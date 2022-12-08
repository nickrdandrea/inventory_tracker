import React, { useDeferredValue, useEffect, useState } from 'react';
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
    const [displayItems, setDisplayItems] = useState(null);

    useEffect(() => {
        const pageEnd = props.currentPage * props.pageSize;
        const pageStart = pageEnd - props.pageSize;
        setDisplayItems(props.items.slice(pageStart, pageEnd));
    },[]);

    return (
        <tbody>
            {displayItems !== null && (
                displayItems.map(item => {
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

function TablePagination(props) {

    const pagItem = () => {
         
    }

    return (
        <Pagination>
            {for (let i = 0; i <= props.numPages; i++) {

            }}
            <Pagination.Prev />
            <Pagination.Item>{1}</Pagination.Item>
            <Pagination.Ellipsis />
            <Pagination.Item>{11}</Pagination.Item>
            <Pagination.Item active>{12}</Pagination.Item>
            <Pagination.Item>{13}</Pagination.Item>
            <Pagination.Ellipsis />
            <Pagination.Item>{20}</Pagination.Item>
            <Pagination.Next />
        </Pagination>
    );
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

    const handlePageChange = (e) => {
        setCurrentPage(e.target.value);
    };
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
                    <ItemTableBody items={filteredItems()} currentPage={currentPage} pageSize={props.pageSize}/>
                ) : (
                    <ItemTableBody items={props.items} currentPage={currentPage} pageSize={props.pageSize}/>
                )}
            </Table>
            <TablePagination currentPage={currentPage} numPages={props.items.length / props.pageSize} />
        </>
    );
}

// function TableHead(props) {

//     const capitlize = (word) => {
//         return word.charAt(0).toUpperCase() + word.slice(1);
//     }

//     <th key={header}>
//         <DropdownButton id="dropdown-button" title={capitlize(props.filter)} variant="outline-dark">
//             {props.filterValues.map(value => {
//                 return (
//                     <Dropdown.Item key={value} as="button" value={value} onClick={props.onFilter}>{value}</Dropdown.Item>
//                 )
//             })}
//         </DropdownButton>
//     </th>

//     return (
//         <thead>
//             <tr>
//                 {props.headers.map(header => {
//                     return (
//                         header === props.filter ? (
//                             <th key={header}>
//                                 <DropdownButton id="dropdown-button" title={capitlize(props.filter)} variant="outline-dark">
//                                     {props.filterValues.map(value => {
//                                         return (
//                                             <Dropdown.Item key={value} as="button" value={value} onClick={props.onFilter}>{value}</Dropdown.Item>
//                                         )
//                                     })}
//                                 </DropdownButton>
//                             </th>
//                         ) : (
//                             <th key={header}>{capitlize(header)}</th>
//                     ))
//                 })}
//             </tr>
//         </thead>
//     )
// }

// function TableBody(props) {
//     return (
//         <tbody>
//         {props.items.map(item => {
//             return (
//                 <tr key={item.id}>
//                     {props.headers.map(header => {
//                         return (
//                             header === props.urlOn ? (
//                                 <td key={header}><a href={item.url}>{item[header]}</a></td>
//                             ) : (
//                                 <td key={header}>{item[header]}</td>
//                             )
//                         )
//                     })}
//                 </tr>
//             )
//         })}
//         </tbody>
//     )
// }

// export default class ItemTable extends React.Component {
//     constructor(props) {
//         super(props);
//         this.state = { selectedFilter: null };
//         this.handleFilterChange = this.handleFilterChange.bind(this);
//     }
    
//     getFilterValues() {
//         const unique = [...new Set(this.props.items.map((item) => item[this.props.filter]))];
//         return unique
//     }

//     filterItems() {
//         return this.props.items.filter(item => item[this.props.filter] === this.state.selectedFilter)
//     }
    
//     handleFilterChange(e) { this.setState({selectedFilter: e.target.value});  }

//     render () {
//         let tableHead = null;
//         let tableBody = null;
//         if (typeof this.props.filter !== "undefined") {
//             const filterValues = this.getFilterValues(this.props.filter)
//             tableHead = <TableHead headers={this.props.headers} filter={this.props.filter} filterValues={filterValues} onFilter={this.handleFilterChange}/>
//         } else {
//             tableHead = <TableHead headers={this.props.headers}/>
//         }

//         if (this.state.selectedFilter !== null) {
//             tableBody = <TableBody headers={this.props.headers} items={this.filterItems()} urlOn={this.props.urlOn}/>
//         } else {
//             tableBody = <TableBody headers={this.props.headers} items={this.props.items} urlOn={this.props.urlOn}/>
//         }

//         return (
//             this.props.items != null && (  
//                 <Table striped bordered hover className='my-2'>
//                     {tableHead}
//                     {tableBody}
//                 </Table>
//             )
//         );
//     }
// }
