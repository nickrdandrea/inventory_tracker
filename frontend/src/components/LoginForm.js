import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { Buffer } from 'buffer';

async function loginUser(username= '', password = '') {
    const url = process.env.REACT_APP_BASE_API_URL + "/login";;
    return fetch(url, {
        method: 'POST',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            Authorization: 'Basic ' + Buffer.from(username + ":" + password).toString('base64')
        }
    }).then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}

export default function LoginForm() {

  const handleFormSubmit = (e) => {
    e.preventDefault();
    let username = e.target[0].value;
    let password = e.target[1].value;
    loginUser(username, password);
  };

  return (
    <Form onSubmit={handleFormSubmit}>
      <Form.Group className="mb-3" controlId="loginFormUsername">
        <Form.Label>Username</Form.Label>
        <Form.Control type="username" placeholder="Enter username" />
      </Form.Group>

      <Form.Group className="mb-3" controlId="loginFormPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Password" />
      </Form.Group>
      <Button variant="primary" type="submit">
        Login
      </Button>
    </Form>
  );
}