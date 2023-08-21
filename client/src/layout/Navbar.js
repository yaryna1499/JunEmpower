import { Grid, Toolbar, Typography, Avatar } from "@mui/material";
import { Link } from "react-router-dom";
import {
  CustomTypography,
  StyledAppBar,
  StyledLink,
} from "../muiStyles/navbar/navbar.styled";

const Navbar = () => {
  return (
    <StyledAppBar position="sticky">
      <Toolbar>
        <Grid container alignItems="center" justifyContent="space-between">
          <Grid item>
            <Typography variant="h5">
              <Link to={"/"} style={{ textDecoration: "none", color: "black" }}>
                <CustomTypography fontWeight={700} variant="title">
                  Jun
                  <Typography variant="span" sx={{ color: "#8ACB88" }}>
                    Empower
                  </Typography>
                </CustomTypography>
              </Link>
            </Typography>
          </Grid>

          <Grid item display="flex" alignItems="center">
            <Typography
              variant="subtitle1"
              color="black"
              sx={{ display: "flex", alignItems: "center" }}
            >
              <Avatar sx={{ marginRight: "0.6rem" }}>U</Avatar>
              <CustomTypography
                fontWeight={500}
                sx={{
                  fontSize: "14px",
                  paddingRight: "6vh",
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
            <StyledLink to={"/login"}>Login</StyledLink>
          </Grid>
        </Grid>
      </Toolbar>
    </StyledAppBar>
  );
};

export default Navbar;
