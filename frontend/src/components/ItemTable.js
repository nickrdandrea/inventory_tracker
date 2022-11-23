import Table from 'react-bootstrap/Table';

export default function ItemTable(props) {
    return (
        <>
        {props.items === null ? (
            <p>There are no items to display.</p>
        ) : (       
            <Table striped bordered hover className='my-2'>
                <thead>
                    <tr>
                    <th>Description</th>
                    <th>Category</th>
                    {/* <th>Date Added</th>
                    <th>Last Updated</th> */}
                    </tr>
                </thead>
                <tbody>
                    {props.items.map(item => {
                        return (
                            <tr key={item.id}>
                            <td><a href={item.url}>{item.description}</a></td>
                            <td>{item.category}</td>
                            {/* <td>{item.date_created}</td>
                            <td>{item.last_updated}</td> */}
                            </tr>
                        )
                    })}
                </tbody>
            </Table>
        )}
        </>
    );
}