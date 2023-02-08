import { useCallback, useEffect, useState } from "react";
import Container from "react-bootstrap/esm/Container";
import SearchBar from "./SearchBar"
import FilterableItemTable from "./ItemTable";
import { getVendorItems, searchVendorItems } from "../api/vendor";

const TABLE_PAGE_SIZE = 25;

export default function InventoryDisplay({ vendor_name }) {
    const [items, setItems] = useState(null);

    useEffect( () => {
        const getItems = async () => getVendorItems(vendor_name, setItems, error => console.log(error))
        getItems()
    }, []);

    const onSubmit = (terms) => {
        let vendorItems = searchVendorItems(vendor_name, terms);
        if (vendorItems) {
            setItems(vendorItems)
        }
    }

    return (
        <Container>
            <SearchBar onSubmit={onSubmit} />
            {items !== null && (
                <FilterableItemTable items={items} pageSize={TABLE_PAGE_SIZE}/>
            )}
        </Container>
    );
}
