import React from "react";
import { NavLink } from "react-router-dom";
import { Typography, Box } from "@mui/material";
import RegistrationForm from "../components/form/RegistrationForm";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import AuthLayout from "../layout/AuthLayout";

const RegistrationPage = () => {
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmitRegister = async (values) => {
    console.log(values);
    navigate("/");
    try {
      // await login(values.email, values.password);
    } catch (error) {
      console.error("Registration error:", error);
    }
  };

  return (
    <AuthLayout>
      <RegistrationForm handleSubmit={handleSubmitRegister} />
      <Box
        sx={{
          fontFamily: "Space Grotesk",
          fontWeight: 700,
          fontSize: "1.2rem",
          marginTop: 8,
        }}
      >
        Have an account?
        <NavLink to="/login" style={{ textDecoration: "none" }}>
          <Typography
            component="span"
            sx={{
              pl: 1.5,
              fontSize: "1.2rem",
              color: "#007AFF",
              "&:hover": { textDecoration: "underline" },
            }}
          >
            Login
          </Typography>
        </NavLink>
      </Box>
    </AuthLayout>
  );
};

export default RegistrationPage;
