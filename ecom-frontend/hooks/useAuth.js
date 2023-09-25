import jwtDecode from "jwt-decode";

export default function useAuth() {
    function logout() {
        localStorage.removeItem('token');
    }
    if(typeof window === 'undefined') return ({
        token: null,
        user: null,
        isLogged: false,
        logout
    })
    const token = localStorage.getItem('token');
    if(!token) {
        return {
            token: null,
            user: null,
            isLogged: false,
            logout
        }
    }
    try {
        const user = jwtDecode(token);
        const isExpried = Date.now() >= user.exp * 1000;
        return {
            token: token,
            user: user,
            isLogged: !isExpried,
            logout
        }
    }
    catch(err) {
        return {
            token: null,
            user: null,
            isLogged: false,
            logout
        }
    }
    
}