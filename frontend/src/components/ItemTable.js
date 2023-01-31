import React, { useMemo, useState } from 'react';
import Table from 'react-bootstrap/Table';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Pagination from 'react-bootstrap/Pagination';

function ItemTableBody({ items }) {  
    return (
        <tbody>
            {items !== null && (
                items.map(item => {
                    return (
                        <tr key={item.id}>
                            <td><a href={item.url}>{item.description}</a></td>
                            <td>{item.category}</td>
                        </tr>
                    )
                }
            ))}
        </tbody>
    )
}

function SimplePagination({currentPage, numOfPages, onClick}) {
    return (
        <Pagination>
            <Pagination.Prev disabled={currentPage == 1} onClick={() => onClick(currentPage - 1)}/>
            {[...Array(numOfPages)].map((x, i) => {
                let pagiNum = i + 1
                return (
                    <Pagination.Item key={pagiNum} active={pagiNum == currentPage} onClick={() => onClick(pagiNum)}>
                        {pagiNum}
                    </Pagination.Item>
                )
            })}
            <Pagination.Next disabled={currentPage == numOfPages} onClick={() => onClick(currentPage + 1)}/>
        </Pagination>
    )
}

function paginateList(list, pageSize) {
    let pageStart = 0
    let pageEnd = pageSize
    let numOfPages = Math.ceil(list.length / pageSize)

    let pages = [...Array(numOfPages)].map((page) => {
        page = list.slice(pageStart, pageEnd)
        pageStart += pageSize
        pageEnd += pageSize
        return page
    })
    return pages
}

function FilterDropDown({ title, filterValues, onClick }) {
    return (
        <DropdownButton id="dropdown-button" title={title} variant="outline-dark">
            <Dropdown.Item key="000" as="button" value="clear" onClick={onClick}>Clear Filter</Dropdown.Item>
            {filterValues.map(value => {
                return (<Dropdown.Item key={value} as="button" value={value} onClick={onClick}>{value}</Dropdown.Item>)
            })}
        </DropdownButton>
    )
}

const filterAttribute = {
    accessor: "category",
    display: "Category"
}

export default function FilterableItemTable({items, pageSize}) {
    const [currentPage, setCurrentPage] = useState(1)
    const [pages, setPages] = useState(paginateList(items, pageSize))

    const filterValues = useMemo(() =>
        [...new Set(items.map((item) => item[filterAttribute.accessor]))],
        [items]
    )

    const handleFilterChange = (e) => {
        setCurrentPage(1)
        if (e.target.value === "clear") {
            setPages(paginateList(items, pageSize))
        } else {
            setPages(paginateList(items.filter(item => item[filterAttribute.accessor] === e.target.value), pageSize))
        }
    }

    const handlePageChange = (value) => {
        setCurrentPage(parseInt(value));
    }

    return (
        <>
            <Table striped bordered hover className='my-2'>
                <thead>
                    <tr>
                        <th>Description</th>
                        <th><FilterDropDown title={filterAttribute.display} filterValues={filterValues} onClick={handleFilterChange} /></th>
                    </tr>
                </thead>
                <ItemTableBody items={pages[currentPage - 1]}/>
            </Table>
            {(pages.length >= 2) ? (
                <SimplePagination currentPage={currentPage} numOfPages={pages.length} onClick={handlePageChange}/> 
            ) : null}
        </>
    );
}
