import React from 'react';
import { Jwt } from 'jsonwebtoken';
import useAuth from 'hooks/useAuth';

export default function ProtectedRoute({ children }) {
    const [loggedIn, setLoggedIn] = React.useState(false);
    const auth = useAuth();
    React.useEffect(() => {
        if (auth.isLogged) {
            setLoggedIn(true);
        }
    }
    , []);

    if (loggedIn) {
        return <>{children}</>
    }
    return <div>Not logged in</div>

}