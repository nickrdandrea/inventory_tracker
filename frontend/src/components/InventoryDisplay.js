import { useCallback, useEffect, useState } from "react";
import Container from "react-bootstrap/esm/Container";
import SearchBar from "./SearchBar"
import FilterableItemTable from "./ItemTable";

const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;
const SEARCH_API_URL = process.env.REACT_APP_BASE_API_URL + "/search?terms=";
const TABLE_PAGE_SIZE = 25;

export default function InventoryDisplay(props) {
    const [items, setItems] = useState(null);
    const [searchTerms, setSearchTerms] = useState(null);

    const fetchItems = useCallback(async (url) => {
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw Error(response.statusText);
            }
            const json = await response.json();
            setItems(json);
        } catch(error) {
            console.log(error);
        }
    }, []);

    const loadEffect = useEffect(() => {
        if (items === null) { 
            fetchItems(BASE_API_URL); 
        } 
    }, [items, fetchItems]);

    const searchEffect = useEffect(() => {
        const prepTerms = (terms) => { return terms.trim().replace(' ', '&'); }
        if (searchTerms !== null) {
            fetchItems(SEARCH_API_URL + prepTerms(searchTerms));
        }
    }, [searchTerms, fetchItems]);

    const onSubmit  = (input) => { setSearchTerms(input); }

    return (
        <Container>
            <SearchBar onSubmit={onSubmit} />
            {items !== null && (
                console.log(items),
                <FilterableItemTable items={items} pageSize={TABLE_PAGE_SIZE}/>
            )}
        </Container>
    );
}
