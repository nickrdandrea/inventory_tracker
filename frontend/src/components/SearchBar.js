import { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';

const SEARCH_API_URL = process.env.REACT_APP_BASE_API_URL + "/search?terms=";

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
    },[searchTerms]);

    function handleChange(event) {
        setInputText(event.target.value);
    }

    function cleanSearchTerms() {
        let cleaned = inputText.trim().replace(' ', '&');
        return(cleaned);
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