import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navigation from './components/Navigation';
import Splash from './pages/SplashPage';
import UserPage from './pages/UserPage';
import ToyTrove from './pages/ToyTrovePage';
import AuthPage from './pages/AuthPage';
import { UserProvider } from './contexts/UserContext';

export default function App() {  
  return (
    <Container fluid className="App">
      <UserProvider>
        <BrowserRouter>
          <Navigation />
          <Routes>
            <Route path="*" element={<Navigate to="/" />} />
            <Route path="/" element={<Splash />} />
            <Route path="/toytrove" element={<ToyTrove />} />
            <Route path="/user/:username" element={<UserPage />} />
            <Route path="/auth" element={<AuthPage />} />
          </Routes>
        </BrowserRouter>
      </UserProvider>
    </Container>
  );
}