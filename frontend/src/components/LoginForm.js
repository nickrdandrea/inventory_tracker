import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { useState } from 'react';
import { useUserDispatch } from '../contexts/UserContext';
import loginUser from '../api/auth';

export default function LoginForm() {
  const [error, setError] = useState(null);
  const dispatch = useUserDispatch();

  const loginSuccess = (userAction) => {
    userAction['type'] = 'logged_in'
    dispatch(userAction);
  };

  const loginFailure = (errorMessage) => setError(errorMessage);

  const handleFormSubmit = (e) => {
    e.preventDefault();
    const credentials = { 
      username: e.target[0].value, 
      password: e.target[1].value 
    }
    loginUser(credentials, loginSuccess, loginFailure);
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