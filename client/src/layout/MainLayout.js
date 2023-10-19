import React from "react";
import Navbar from "./Navbar/Navbar";
import { Box } from "@mui/material";

const MainLayout = ({ children }) => {
  return (
    <>
      <Navbar />
      <Box paddingTop="7rem">{children}</Box>
    </>
  );
};

export default MainLayout;
