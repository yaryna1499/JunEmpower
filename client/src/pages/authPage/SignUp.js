import { useNavigate } from "react-router-dom";
import { Typography, Box, Link } from "@mui/material";
import RegistrationForm from "../../components/form/SignUpForm";
import { useAuth } from "../../context/AuthContext";
import { AuthContainer } from "./auth.styled";

const SignUp = () => {
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmitRegister = async (values) => {
    try {
      await register(values.username, values.email, values.password);
      navigate("/signin");
    } catch (error) {
      console.error("Registration error:", error);
    }
  };

  return (
    <AuthContainer>
      <Box display="flex" flexDirection="column" gap="20px">
        <Typography component="h1" variant="title">
          Sign up*
        </Typography>
        <RegistrationForm handleSubmit={handleSubmitRegister} />

        <Typography sx={{ textAlign: "center" }}>
          Have an account?
          <Link href="/signin" variant="body2" sx={{ pl: "2%" }}>
            {"Sign In"}
          </Link>
        </Typography>
      </Box>
    </AuthContainer>
  );
};

export default SignUp;
