import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Table from 'react-bootstrap/Table';

const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;

export default function ItemFeed(props) {
  const [items, setItems] = useState([]);
  useEffect (() => {
    (async () => {
      const response = await fetch(BASE_API_URL, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      if (response.ok) {
        const results = await response.json();
        setItems(results);    
      }
      else {
        setItems(null)
      }
    })();
  }, []);

  return (
    <Container>
      {items === null ? (
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
            {items.map(item => {
              return (
                <tr key={item.id}>
                  <td><a href={item.url}>{item.description}</a></td>
                  <td>{item.category}</td>
                  {/* <td>{item.date_created}</td>
                  <td>{item.last_updated}</td> */}
                </tr>
              )
            })
          }
          </tbody>
        </Table>
      )}

    </Container>

  );
}
