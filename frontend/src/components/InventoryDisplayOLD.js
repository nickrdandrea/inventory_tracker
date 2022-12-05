import { useEffect, useState } from "react";
import Container from "react-bootstrap/esm/Container";
import SearchBar from "../components/SearchBar"
import ItemTable from "./ItemTable";

const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;

export default function InventoryDisplay(props) {
    const [allItems, setAllItems] = useState(null);
    const [displayedItems, setDisplayedItems] = useState([]);
    const [searchedItems, setSearchedItems] = useState();

    useEffect(() => {
        (async () => {
            if (allItems === null) {
                let response = await fetch(BASE_API_URL, {
                    headers: {
                      'Content-Type': 'application/json'
                    }
                });
                if (response.ok) {
                    let results = await response.json();
                    setAllItems(results);    
                    setDisplayedItems(results);
                } else {
                    setAllItems(null);
                }
            }
        })();
    },[]);

    function searchCallback(items) {
        setSearchedItems(items);
        setDisplayedItems(items);
    }

    function filterDisplayed(value) {
        return displayedItems.filter((v,i,a)=>a.findIndex(v2=>[value].every(k=>v2[k] ===v[k]))===i)
    }


    return (
        <Container>
            <SearchBar vendor={props.vendor} callback={searchCallback}/>
            <ItemTable items={displayedItems} headers={["description", "category"]} filter={"category"}/>
        </Container>
    );
}