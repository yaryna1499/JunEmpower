import React from "react";
import { NavLink } from "react-router-dom";
import { Button } from "@mui/material";

const CustomButton = ({ to, isActive, children }) => {
  return (
    <NavLink to={to} style={{ width: "50%" }}>
      <Button
        sx={{
          backgroundColor: isActive ? "orange" : "#EEEEEF",
          width: "100%",
          fontFamily: "Space Grotesk",
          fontWeight: 700,
        }}
      >
        {children}
      </Button>
    </NavLink>
  );
};

export default CustomButton;
