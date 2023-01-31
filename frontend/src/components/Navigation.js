import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import { NavLink } from 'react-router-dom';
import Container from 'react-bootstrap/Container';

export default function Navigation() {
  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Container>
        <Navbar.Brand>
          <Nav.Link as={NavLink} to="/">Inventory Tracker</Nav.Link>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto ms-lg-3">
            <Nav.Link href="/toytrove">ToyTrove</Nav.Link>
            <Nav.Link href="/">Meeplemart</Nav.Link>
          </Nav>
          <Nav>
            <Nav.Item>
              <Nav.Link as={NavLink} to="/auth">Login</Nav.Link>
            </Nav.Item>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
