import React from "react";
import Navbar from "./Navbar";

const PrivateLayout = ({ children }) => {
  return (
    <>
      <Navbar />
      {children}
    </>
  );
};

export default PrivateLayout;
