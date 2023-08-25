import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import Navbar from "../layout/Navbar/Navbar";
import { Box } from "@mui/material";

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  return (
    <>
      <Navbar />
      <Box paddingTop="3rem">{children}</Box>
    </>
  );
};

export default ProtectedRoute;
