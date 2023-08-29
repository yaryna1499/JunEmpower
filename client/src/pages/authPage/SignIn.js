import { Box, Typography, Link } from "@mui/material";
import LoginForm from "../../components/form/LoginForm";
import { AuthContainer } from "./auth.styled";
import { useAuth } from "../../context/AuthContext";
import { useNavigate } from "react-router-dom";

const SignIn = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmitLogin = async (values) => {
    try {
      await login(values.username, values.password);
      navigate("/profile");
    } catch (error) {
      console.error("Login error:", error);
    }
  };

  return (
    <AuthContainer component="main">
      <Box display="flex" flexDirection="column" gap="20px">
        <Typography component="h1" variant="title">
          Sign in*
        </Typography>
        <LoginForm handleSubmit={handleSubmitLogin} />

        <Typography sx={{ textAlign: "center" }}>
          Don't have an account?
          <Link href="/signup" variant="body2" sx={{ pl: "2%" }}>
            {"Sign Up"}
          </Link>
        </Typography>
      </Box>
    </AuthContainer>
  );
};

export default SignIn;
