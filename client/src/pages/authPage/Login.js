import React from "react";
import { NavLink } from "react-router-dom";
import { Typography, Box, Link } from "@mui/material";
import LoginForm from "../../components/form/LoginForm";
import { useAuth } from "../../context/AuthContext";
import { useNavigate } from "react-router-dom";
import AuthLayout from "../../layout/AuthLayout";
import { AuthBox } from "./auth.styled";

const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmitLogin = async (values) => {
    try {
      await login(values.email, values.password);
      navigate("/profile");
    } catch (error) {
      console.error("Login error:", error);
    }
  };

  return (
    <AuthLayout>
      <LoginForm handleSubmit={handleSubmitLogin} />
      <AuthBox>
        <Box>
          Forgot password?
          <Link
            href="#"
            variant="body2"
            sx={{
              textDecoration: "none",
              pl: 1.5,
              fontSize: "1.2rem",
              color: "#007AFF",
              "&:hover": { textDecoration: "underline" },
            }}
          >
            Remember
          </Link>
        </Box>
        <Box>
          Don't have an account?
          <NavLink to="/signup" style={{ textDecoration: "none" }}>
            <Typography
              component="span"
              sx={{
                pl: 1.5,
                fontSize: "1.2rem",
                color: "#007AFF",
                "&:hover": { textDecoration: "underline" },
              }}
            >
              Sign Up
            </Typography>
          </NavLink>
        </Box>
      </AuthBox>
    </AuthLayout>
  );
};

export default Login;
