import { useEffect, useState } from "react";
import Container from "react-bootstrap/esm/Container";
import SearchBar from "./SearchBar"
import FilterableItemTable from "./ItemTable";

const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;
const SEARCH_API_URL = process.env.REACT_APP_BASE_API_URL + "/search?terms=";

export default function InventoryDisplay(props) {
    const [items, setItems] = useState(null);
    const [searchTerms, setSearchTerms] = useState(null);

    const fetchItems = async (search=false) => {
        let url = BASE_API_URL
        search && (
            url = SEARCH_API_URL + searchTerms
        )
        let response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.ok) {
            let results = await response.json();
            setItems(results);    
        } else {
            setItems(null);
        }
    }

    useEffect(() => {
        if (items === null) { fetchItems() }
        if (searchTerms !== null) {fetchItems(true)}
    },[items, searchTerms, fetchItems]);

    return (
        <Container>
            {items !== null && (
                <FilterableItemTable items={items} />
            )}
        </Container>
    );
}


// useEffect(() => {
//     (async () => {
//         if (allItems === null) {
//             let response = await fetch(BASE_API_URL, {
//                 headers: {
//                   'Content-Type': 'application/json'
//                 }
//             });
//             if (response.ok) {
//                 let results = await response.json();
//                 setAllItems(results);    
//                 setDisplayedItems(results);
//             } else {
//                 setAllItems(null);
//             }
//         }
//     })();
// },[]);
