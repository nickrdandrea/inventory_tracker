import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navigation from './components/Navigation';
import Splash from './pages/Splash';
import UserPage from './pages/UserPage';
import ToyTrove from './pages/ToyTrove';
import AuthPage from './pages/AuthPage';
import UserProvider from './UserContext';

export default function App() {  
  return (
    <Container fluid className="App">
      <UserProvider>
        <BrowserRouter>
          <Navigation />
          <Routes>
            <Route path="/" element={<Splash />} />
            <Route path="/toytrove" element={<ToyTrove />} />
            <Route path="/user/:username" element={<UserPage />} />
            <Route path="/auth" element={<AuthPage />} />
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </BrowserRouter>
      </UserProvider>
    </Container>
  );
}