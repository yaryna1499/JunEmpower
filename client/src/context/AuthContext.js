import React, { createContext, useContext, useState } from "react";
import axios from "axios";
import { useCookies } from "react-cookie";

const url = "https://yaryna1499.pythonanywhere.com";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [setCookie, removeCookie] = useCookies(["token"]);

  const handleAuthentication = async (data, endpoint) => {
    try {
      const response = await axios.post(`${url}${endpoint}`, data);

      if (endpoint === "/login/") {
        const token = response.data.access_token;
        setCookie("token", token, { path: "/" });
        setIsAuthenticated(true);
      }

      return response;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  const register = async (username, email, password) => {
    await handleAuthentication({ username, email, password }, "/register/");
  };

  const login = async (username, password) => {
    await handleAuthentication({ username, password }, "/login/");
  };

  const logout = () => {
    removeCookie("token");
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, register, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
