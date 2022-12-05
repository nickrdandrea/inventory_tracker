import React from 'react';
import Table from 'react-bootstrap/Table';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

// function FilterDropdown(props) {
//     return(
//         <DropdownButton id="dropdown-button" title={props.filter} variant="outline-dark">
//             {console.log(props.filterValues)}
//             {props.filterValues.map(value => {
//                 return (
//                     <Dropdown.Item key={value} as="button" onClick={props.onFilter}>{value}</Dropdown.Item>
//                 )
//             })}
//         </DropdownButton>
//     )
// }

function TableHead(props) {

    const capitlize = (word) => {
        return word.charAt(0).toUpperCase() + word.slice(1);
    }

    return (
        <thead>
            <tr>
                {props.headers.map(header => {
                    return (
                        header === props.filter ? (
                            <th key={header}>
                                <DropdownButton id="dropdown-button" title={capitlize(props.filter)} variant="outline-dark">
                                    {props.filterValues.map(value => {
                                        return (
                                            <Dropdown.Item key={value} as="button" value={value} onClick={props.onFilter}>{value}</Dropdown.Item>
                                        )
                                    })}
                                </DropdownButton>
                            </th>
                        ) : (
                            <th key={header}>{capitlize(header)}</th>
                    ))
                })}
            </tr>
        </thead>
    )
}

function TableBody(props) {
    return (
        <tbody>
        {props.items.map(item => {
            return (
                <tr key={item.id}>
                    {props.headers.map(header => {
                        return (
                            header === props.urlOn ? (
                                <td key={header}><a href={item.url}>{item[header]}</a></td>
                            ) : (
                                <td key={header}>{item[header]}</td>
                            )
                        )
                    })}
                </tr>
            )
        })}
        </tbody>
    )
}

export default class ItemTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = { selectedFilter: null };
        this.handleFilterChange = this.handleFilterChange.bind(this);
    }
    
    getFilterValues(filter) {
        const unique = [...new Set(this.props.items.map((item) => item[filter]))];
        return unique
    }

    filterItems(filter) {
        return this.props.items.filter(item => item[this.props.filter] === this.state.selectedFilter)
    }
    
    handleFilterChange(e) { this.setState({selectedFilter: e.target.value});  }

    render () {
        let tableHead = null;
        let tableBody = null;
        if (typeof this.props.filter !== "undefined") {
            const filterValues = this.getFilterValues(this.props.filter)
            tableHead = <TableHead headers={this.props.headers} filter={this.props.filter} filterValues={filterValues} onFilter={this.handleFilterChange}/>
        } else {
            tableHead = <TableHead headers={this.props.headers}/>
        }

        if (this.state.selectedFilter !== null) {
            tableBody = <TableBody headers={this.props.headers} items={this.filterItems()} urlOn={this.props.urlOn}/>
        } else {
            console.log("hi")
            tableBody = <TableBody headers={this.props.headers} items={this.props.items} urlOn={this.props.urlOn}/>
        }

        return (
            this.props.items != null && (  
                <Table striped bordered hover className='my-2'>
                    {tableHead}
                    {tableBody}
                </Table>
            )
        );
    }
}

// export default function ItemTable(props) {
//     const [categories, setCategories] = useState([])
//     const [items, setItems] = useState([])

//     useEffect(() => {
//         let  itemCategories = props.items.filter(( item, i, array) => array.findIndex(item2 => ["category"].every(p => item2[p] === item[p])) === i);
//         setCategories(itemCategories.map(item => item.category))
//         setItems(props.items)
//     },[props.items]);

//     return (
//         <>
//         {props.items === null ? (
//             <p>There are no items to display.</p>
//         ) : (       
//             <Table striped bordered hover className='my-2'>
//                 <thead>
//                     <tr>
//                     <th>Description</th>
//                     <th><CategoryFilter options={categories}/></th>
//                     {/* <th>Date Added</th>
//                     <th>Last Updated</th> */}
//                     </tr>
//                 </thead>
//                 <tbody>
//                     {props.items.map(item => {
//                         return (
//                             <tr key={item.id}>
//                             <td><a href={item.url}>{item.description}</a></td>
//                             <td>{item.category}</td>
//                             {/* <td>{item.date_created}</td>
//                             <td>{item.last_updated}</td> */}
//                             </tr>
//                         )
//                     })}
//                 </tbody>
//             </Table>
//         )}
//         </>
//     );
// }