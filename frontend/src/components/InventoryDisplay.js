import React from "react";
import ItemTable from "./ItemTable";
import Container from "react-bootstrap/esm/Container";


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
        this.renderItemTable = this.renderItemTable.bind(this);
    }

    async fetchItems() {
        try {
            const response = await fetch(BASE_API_URL);
            if (!response.ok) {
              throw Error(response.statusText);
            }
            const json = await response.json();

            this.setState({ items: json });
            console.log("Fetch", this.state.items);
        } catch(error) {
            console.log(error);
        }
    }

    componentDidMount() {
        this.fetchItems();
    }

    renderItemTable() {
        const tFilter = "category";
        const tHeaders = ["description", "category"];
        const tURLOn = "description";

        if (this.state.items !== null) {
            return <ItemTable items={this.state.items} headers={tHeaders} filter={tFilter} urlOn={tURLOn}/>
        } else {
            return <h1>No items to display</h1>
        }
    }

    render() {
        const tFilter = "category";
        const tHeaders = ["description", "category"];
        const tURLOn = "description";

        return (
            <Container>
                {this.state.items !== null ? (
                    <ItemTable items={this.state.items} headers={tHeaders} filter={tFilter} urlOn={tURLOn}/>
                 ) : (
                    <h1>No items to display</h1>
                )}
            </Container>
        );
    }
}