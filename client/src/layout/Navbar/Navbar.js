import { Grid, Toolbar, Typography, Avatar, Button } from "@mui/material";
import { Link, useNavigate } from "react-router-dom";
import { CustomTypography, StyledAppBar, StyledLink } from "./navbar.styled";
import { useAuth } from "../../context/AuthContext";

const Navbar = () => {
  const { isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/signin");
  };

  return (
    <StyledAppBar position="fixed">
      <Toolbar>
        <Grid container alignItems="center" justifyContent="space-between">
          <Grid item>
            <Typography variant="h5">
              <Link to={"/"} style={{ textDecoration: "none", color: "black" }}>
                <CustomTypography fontWeight={700}>
                  Jun
                  <Typography variant="span" sx={{ color: "#8ACB88" }}>
                    Empower
                  </Typography>
                </CustomTypography>
              </Link>
            </Typography>
          </Grid>

          <Grid item display="flex" alignItems="center" gap="1rem">
            <Typography
              variant="subtitle1"
              color="black"
              sx={{ display: "flex", alignItems: "center" }}
            >
              <Avatar sx={{ mr: "0.6rem" }}>U</Avatar>
              <CustomTypography
                fontWeight={500}
                sx={{
                  fontSize: "14px",
                  pr: "6vh",
                }}
              >
                Hello,
                <br />
                <Typography
                  variant="span"
                  sx={{ fontWeight: 700, fontSize: "17px" }}
                >
                  My User Name
                </Typography>
              </CustomTypography>
            </Typography>

            <StyledLink to={"/profile"}>Profile</StyledLink>

            {isAuthenticated ? (
              <Button variant="outlined" onClick={handleLogout}>
                Log out
              </Button>
            ) : (
              <StyledLink to={"/signin"}>Sign In</StyledLink>
            )}
          </Grid>
        </Grid>
      </Toolbar>
    </StyledAppBar>
  );
};

export default Navbar;
