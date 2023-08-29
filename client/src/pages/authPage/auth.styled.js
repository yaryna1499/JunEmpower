import { styled } from "@mui/system";
import { Box, Container } from "@mui/material";

export const AuthBox = styled(Box)(({ theme }) => ({
  fontFamily: "Space Grotesk",
  fontWeight: 700,
  fontSize: "1.2rem",
  marginTop: "2rem",
}));

export const AuthContainer = styled(Container)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  justifyContent: "center",
  height: "100vh",
  maxWidth: "515px !important",
}));
