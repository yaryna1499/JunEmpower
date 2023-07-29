import React from "react";
import { Navigate, Outlet } from "react-router-dom";
import Navbar from "../layout/Navbar"

const RequireAuth = () => {
  const auth = true;

  if (!auth) {
    return <Navigate to="/login" />;
  }
  return (
    <>
      <Navbar />
      <Outlet />
    </>
  );
};

export default RequireAuth;
