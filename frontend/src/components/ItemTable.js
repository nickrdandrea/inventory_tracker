import React, { useState } from 'react';
import Table from 'react-bootstrap/Table';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Pagination from 'react-bootstrap/Pagination';

function FilterDropDown(props) {
    return (
        <DropdownButton id="dropdown-button" title={props.title} variant="outline-dark">
            {props.filterValues.map(value => {
                return (<Dropdown.Item key={value} as="button" value={value} onClick={props.onFilter}>{value}</Dropdown.Item>)
            })}
        </DropdownButton>
    )
}

function ItemTableBody(props) {  
    return (
        <tbody>
            {props.items !== null && (
                props.items.map(item => {
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

function SimplePagination(props) {
    return (
        <Pagination>
            <Pagination.Prev disabled={props.currentPage == 1} onClick={() => props.onClick(props.currentPage - 1)}/>
            {[...Array(props.numPages)].map((x, i) => {
                let pagiNum = i + 1
                return (
                    <Pagination.Item key={pagiNum} active={pagiNum == props.currentPage} onClick={() => props.onClick(pagiNum)}>
                        {pagiNum}
                    </Pagination.Item>
                )
            })}
            <Pagination.Next disabled={props.currentPage == props.numPages} onClick={() => props.onClick(props.currentPage + 1)}/>
        </Pagination>
    )
}

export default function FilterableItemTable(props) {
    const [selectedFilter, setSelectedFilter] = useState(null)
    const [currentPage, setCurrentPage] = useState(1)

    const getFilterValues = (filter) => {
        return [...new Set(props.items.map((item) => item[filter]))];
    }

    const filteredItems = () => {
        return props.items.filter(item => item["category"] === selectedFilter)
    }

    const handleFilterChange = (e) => {
        setSelectedFilter(e.target.value);
    }

    const handlePageChange = (value) => {
        setCurrentPage(parseInt(value));
    }

    const getNumPages = () => {
        return Math.ceil(props.items.length / props.pageSize)
    }

    const getPageItems = (items) => {
        let pageEnd = currentPage * props.pageSize;
        let pageStart = pageEnd - props.pageSize;
        return items.slice(pageStart, currentPage * props.pageSize)
    }

    return (
        <>
            <Table striped bordered hover className='my-2'>
                <thead>
                    <tr>
                        <th>Description</th>
                        <th><FilterDropDown title="Category" filterValues={getFilterValues("category")} onFilter={handleFilterChange} /></th>
                    </tr>
                </thead>
                {selectedFilter !== null ? (
                    <ItemTableBody items={getPageItems(filteredItems())}/>
                ) : (
                    <ItemTableBody items={getPageItems(props.items)}/>
                )}
            </Table>
            <SimplePagination currentPage={currentPage} numPages={getNumPages()} onClick={handlePageChange}/>
        </>
    );
}
