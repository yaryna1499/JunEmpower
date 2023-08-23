import React from "react";
import { NavLink, useLocation } from "react-router-dom";
import { Typography, Container, Box, ButtonGroup } from "@mui/material";
import CustomButton from "../components/helper/AuthButton";

const AuthLayout = ({ children }) => {
  const location = useLocation();
  const isRegisterPage = location.pathname === "/signup";
  const isLoginPage = location.pathname === "/login";

  return (
    <Container maxWidth="xs">
      <NavLink
        to="/"
        style={{
          paddingTop: "1rem",
          textDecoration: "none",
          display: "flex",
          alignItems: "center",
          cursor: "pointer",
          fontSize: "1.2rem",
          color: "#000000",
        }}
      >
        Home page
      </NavLink>

      <Box
        sx={{
          mt: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Typography component="h2" variant="title" sx={{ mb: 3 }}>
          Jun
          <Typography variant="span" color="#8ACB88">
            Empower
          </Typography>
        </Typography>
        <ButtonGroup
          disableElevation
          variant="contained"
          aria-label="Disabled elevation buttons"
          sx={{ width: "100%" }}
        >
          <CustomButton to="/signup" isActive={isRegisterPage}>
            Sign Up
          </CustomButton>

          <CustomButton to="/login" isActive={isLoginPage}>
            Login
          </CustomButton>
        </ButtonGroup>
      </Box>
      {children}
    </Container>
  );
};

export default AuthLayout;
