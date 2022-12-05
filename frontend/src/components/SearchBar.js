import React, { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';

const SEARCH_API_URL = process.env.REACT_APP_BASE_API_URL + "/search?terms=";

// export default class SearchBar extends React.Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             value: "",
//             searchTerms: ""
//         };
//         this.handleChange = this.handleChange.bind(this);
//         this.handleSubmit = this.handleSubmit.bind(this);
//     }

//     searchTerms() {
//         return this.state.value.trim().replace(' ', '&');
//     }
    
//     handleChange(e) {    this.setState({value: e.target.value});  }
      
//     handleSubmit(e) {
//         let params = this.searchTerms()
//         fetch(SEARCH_API_URL.concat(params))
//         .then(response => response.json())
//         .then(data => {
//             this.setState({synList:data})
//         });
//     }

// }
export default function SearchBar(props) {
    const [inputText, setInputText] = useState()
    const [searchTerms, setSearchTerms] = useState()

    useEffect(() => {
        (async () => {
            if (searchTerms != null) {
                let searchURL = SEARCH_API_URL + searchTerms
                let response = await fetch(searchURL);
                if (response.ok) {
                    let results = await response.json();
                    props.callback(results);
                } else {
                    props.callback(null);
                }
            }
        })();
    },[searchTerms, props]);

    function cleanSearchTerms() {
        return inputText.trim().replace(' ', '&');
    }

    function handleChange(event) {
        setInputText(event.target.value);
    }

    function handleClick() {
        let searchTerms = cleanSearchTerms();
        setSearchTerms(searchTerms);
    }

    return (
        <>
        <InputGroup className="my-3">
            <Form.Control placeholder="Search" onChange={handleChange}/>
            <Button variant="outline-secondary" type="button" onClick={handleClick}>Submit</Button>
        </InputGroup>
        </>
    );
}