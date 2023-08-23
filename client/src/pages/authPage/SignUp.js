import React from "react";
import { NavLink } from "react-router-dom";
import { Typography } from "@mui/material";
import RegistrationForm from "../../components/form/RegistrationForm";
import { useAuth } from "../../context/AuthContext";
import { useNavigate } from "react-router-dom";
import AuthLayout from "../../layout/AuthLayout";
import { AuthBox } from "./auth.styled";

const SignUp = () => {
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmitRegister = async (values) => {
    // navigate("/");
    try {
      await register(values.username, values.email, values.password);
    } catch (error) {
      console.error("Registration error:", error);
    }
  };

  return (
    <AuthLayout>
      <RegistrationForm handleSubmit={handleSubmitRegister} />
      <AuthBox>
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
      </AuthBox>
    </AuthLayout>
  );
};

export default SignUp;
