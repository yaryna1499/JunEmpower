import { AppBar, Typography } from "@mui/material";
import { styled } from "@mui/system";
import { Link } from "react-router-dom";

export const StyledAppBar = styled(AppBar)(({ theme }) => ({
  backgroundColor: "#EFEFEE",
  color: "black",
  paddingLeft: "3%",
  paddingRight: "3%",
  boxSizing: "border-box",
}));

export const StyledLink = styled(Link)(({ theme }) => ({
  textDecoration: "none",
  marginLeft: "16px",
  color: "green",
  fontFamily: "DM Sans, sans-serif",
  fontSize: "20px",
}));

export const CustomTypography = styled(Typography)`
  font-family: "Space Grotesk";
  font-size: 1.7rem;
  font-weight: ${({ fontWeight }) => fontWeight || 400};
`;