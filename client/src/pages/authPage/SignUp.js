import { NavLink, useNavigate } from "react-router-dom";
import { Typography } from "@mui/material";
import RegistrationForm from "../../components/form/SignUpForm";
import { useAuth } from "../../context/AuthContext";
import AuthLayout from "../../layout/AuthLayout";
import { AuthBox } from "./auth.styled";
import { useState } from "react";
import Modal from "../../components/helper/CustomModal";

const SignUp = () => {
  const [isSuccessModalOpen, setIsSuccessModalOpen] = useState(false);
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmitRegister = async (values) => {
    try {
      await register(values.username, values.email, values.password);
      setIsSuccessModalOpen(true);
    } catch (error) {
      console.error("Registration error:", error);
    }
  };

  const handleCloseModal = () => {
    setIsSuccessModalOpen(false);
    navigate("/login");
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

      <Modal
        isSuccessModalOpen={isSuccessModalOpen}
        handleCloseModal={handleCloseModal}
      />
    </AuthLayout>
  );
};

export default SignUp;
