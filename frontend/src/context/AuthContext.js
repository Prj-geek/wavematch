import { createContext, useContext, useState } from "react";
import { setToken, clearToken, getToken } from "../api/wavematchApi";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setAuthToken] = useState(getToken());

  const login = (token) => {
    setToken(token);
    setAuthToken(token);
  };

  const logout = () => {
    clearToken();
    setAuthToken(null);
  };

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
