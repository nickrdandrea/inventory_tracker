import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { InputGroup } from 'react-bootstrap';

export default function SearchBar(props) {
    const [inputText, setInputText] = useState(null)

    const onSubmit = (e) => {
        e.preventDefault()
        if (inputText !== null) {
            props.onSubmit(inputText)
        }
    }

    const onChange = (e) => {setInputText(e.target.value)}

    return (
        <Form className="my-3" onSubmit={onSubmit}>
            <InputGroup className="mb-3">
                <Form.Control placeholder="Search" onChange={onChange}/>
                <Button variant="outline-dark" type="submit">Search</Button>
            </InputGroup>
        </Form>
    );
}