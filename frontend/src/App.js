import Container from 'react-bootstrap/Container';
import Header from './components/Header';
import Body from './components/Body';
import ItemFeed from './components/ItemFeed';

export default function App() {
  return (
    <Container fluid className="App">
      <Header />
      <Body sidebar>
        <ItemFeed />
      </Body>
    </Container>
  );
}
