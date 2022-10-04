import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navigation from './components/Navigation';
import FeedPage from './pages/FeedPage';
import VendorsPage from './pages/VendorsPage';
import UserPage from './pages/UserPage';
import LoginPage from './pages/LoginPage';

export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <Navigation />
        <Routes>
          <Route path="/" element={<FeedPage />} />
          <Route path="/vendors" element={<VendorsPage />} />
          <Route path="/user/:username" element={<UserPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </Container>
  );
}