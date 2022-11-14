import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navigation from './components/Navigation';
import Splash from './pages/Splash';
import VendorsPage from './pages/VendorsPage';
import UserPage from './pages/UserPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import ToyTrove from './pages/ToyTrove';

export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <Navigation />
        <Routes>
          <Route path="/" element={<Splash />} />
          <Route path="/toytrove" element={<ToyTrove />} />
          <Route path="/user/:username" element={<UserPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </Container>
  );
}