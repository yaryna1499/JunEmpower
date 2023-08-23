import React, { createContext, useContext, useState } from "react";
import axios from "axios";

const url = "https://yaryna1499.pythonanywhere.com";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(true);

  const handleAuthentication = async (data, endpoint) => {
    try {
      const response = await axios.post(`${url}${endpoint}`, data);
      console.log(response);
      // const token = response.data.token;
      // localStorage.setItem("token", token);
      // setIsAuthenticated(true);
    } catch (error) {
      console.error(error);
    }
  };

  const register = async (username, email, password) => {
    await handleAuthentication({ username, email, password }, "/register/");
  };

  const login = async (username, password) => {
    await handleAuthentication({ username, password }, "/login");
  };

  const logout = () => {
    localStorage.removeItem("token");
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
