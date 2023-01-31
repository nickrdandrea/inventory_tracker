import Body from '../components/Body';
import LoginForm from '../components/LoginForm';
import { createContext, useContext, useState } from 'react';

const UserContext = createContext(null)

export default function AuthPage() {
  const [user, setUser] = useState(null);
  return (
    <Body>
      <UserContext.Provider value={user}>
        <LoginForm />
      </UserContext.Provider>
    </Body>
  );
}