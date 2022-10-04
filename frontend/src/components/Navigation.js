import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavLink from 'react-bootstrap/NavLink';
import Container from 'react-bootstrap/Container';

export default function Navigation() {
  return ( 
    <Navbar bg="light" sticky="top" className="Header">
      <Container>
        <Navbar.Brand>
            <Nav.Link as={NavLink} to="/">Inv Tracker</Nav.Link>
          </Navbar.Brand>
          <Navbar.Toggle />
          <Nav>
            <Nav.Item>
              <Nav.Link as={NavLink} to="/vendors">Vendors</Nav.Link>
            </Nav.Item>
          </Nav>
        <Navbar.Collapse>
          <Nav className="justify-content-end">
            <Nav.Item>
              <Nav.Link as={NavLink} to="/">Login</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link as={NavLink} to="/">Register</Nav.Link>
            </Nav.Item>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
