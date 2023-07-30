import React from "react";
import Navbar from "./Navbar";

const LayoutWithNavbar = ({ children }) => {
  return (
    <>
      <Navbar />
      {children}
    </>
  );
};

export default LayoutWithNavbar;
