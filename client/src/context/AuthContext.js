import React, { createContext, useContext, useState } from "react";
import axios from "axios";
import { useCookies } from "react-cookie";

const url = "https://yaryna1499.pythonanywhere.com";

const AuthContext = createContext();

const client = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState([]);


const handleAuthentication = async (data, endpoint) => {
  try {
    const response = await fetch(`${url}${endpoint}`, {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include", // Enable sending and receiving cookies
    });

    if (endpoint === "/login/") {
      if (response.status === 200) {
        const user = (await response.json()).user;
        let sessionid = response.cookies["sessionid"];
        
        // Set the user and isAuthenticated state
        setUser(user);
        setIsAuthenticated(true);
      } else {
        // Handle authentication failure, e.g., show an error message
        // or clear user and isAuthenticated state
        // setUser(null);
        // setIsAuthenticated(false);
      }
    }

    return response;
  } catch (error) {
    console.error(error);
    throw error;
  }
};
  const register = async (username, email, password) => {
    await handleAuthentication({ username, email, password }, "/user/");
  };

  const login = async (username, password) => {
    await handleAuthentication({ username, password }, "/login/");
  };

  const logout = async () => {
    await axios.get(`${url}/logout/`)
    // removeCookie("token");
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
