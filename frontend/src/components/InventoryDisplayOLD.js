import React from "react";
import FilterableItemTable from "./ItemTable";
import Container from "react-bootstrap/esm/Container";
import SearchBar from "./SearchBar";


const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;
const SEARCH_API_URL = process.env.REACT_APP_BASE_API_URL + "/search?terms=";

export default class InventoryDisplay extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            items: null,
            searchTerms: null
        };
        this.fetchItems = this.fetchItems.bind(this);
    }

    async fetchItems(vendor, search = false) {
        const url = BASE_API_URL
        search && (
            url = SEARCH_API_URL + searchTerms
        )

        try {
            const response = await fetch(url);
            if (!response.ok) {
              throw Error(response.statusText);
            }
            const json = await response.json();
            this.setState({ items: json });
        } catch(error) {
            console.log(error);
        }
    }

    async fetchSearch() {
        try {
            const response = await fetch(SEARCH_API_URL);
            if (!response.ok) {
              throw Error(response.statusText);
            }
            const json = await response.json();
            this.setState({ items: json });
        } catch(error) {
            console.log(error);
        }
    }

    componentDidMount() {
        this.fetchItems();
    }

    render() {
        return (
            <Container>
                <SearchBar />
                {this.state.items !== null && (
                    <FilterableItemTable items={this.state.items} />
                 )}
            </Container>
        );
    }
}