import { Button, Typography } from "@mui/material";
import { Box } from "@mui/system";
import { styled } from "@mui/material/styles";
import { Link as RouterLink } from "react-router-dom";
import image from "../assets/6363147.jpg";

const BoxStyle = styled(Box)(({ theme }) => ({
  maxHeight: "calc(100vh - var(--navbar-height))",
  textAlign: "center",
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",

  "& h4": {
    paddingTop: "5vh",
  },

  "& img": {
    maxWidth: 450,
  },
  "& .MuiButton-root": {
    backgroundColor: "#198416cd",
    color: "#fff",
    marginTop: 20,
  },
}));

const NotFound = () => {
  return (
    <>
      <BoxStyle>
        <Typography variant="h4">Sorry, page not found!</Typography>
        <img src={image} alt="404 Error" loading="lazy" />
        <Button
          to="/"
          variant="contained"
          component={RouterLink}
          size="large"
          disableElevation
        >
          Go to Home
        </Button>
      </BoxStyle>
    </>
  );
};

export default NotFound;
