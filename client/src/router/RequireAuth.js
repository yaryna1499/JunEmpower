import React from "react";
import { Navigate } from "react-router-dom";

const isAuthenticated = false; 

const RequireAuth = ({ children }) => {
  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  return children; 
};

export default RequireAuth;
