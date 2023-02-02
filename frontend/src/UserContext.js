import { createContext, useReducer } from "react";

export const UserContext = createContext(null);
export const UserDispatchContext = createContext(null);

const initialUser = {
    username: null,
    userID: null,
    token: null,
    loggedIn: false
};

function userReducer(state, action) {
    switch(action.type) {
        case 'logged_in': {
            return {
                user: {
                username: action.username,
                id: action.id,
                token: action.token,
                loggedIn: true
                }
            }
        }
        case 'logged_out': {
            return { initialUser }
        }
        default: {
            throw Error('Unknown action: ' + action.type);
        }
    }
};

export default function UserProvider({ children }) {
    const [user, dispatch] = useReducer(userReducer, initialUser);

    return (
        <UserContext.Provider value={user} >
            <UserDispatchContext.Provider value={dispatch} >
                {children}
            </UserDispatchContext.Provider>
        </UserContext.Provider>
    )
};