import { AppBar, Grid, Toolbar, Typography, Avatar } from "@mui/material";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <AppBar
      position="sticky"
      style={{
        backgroundColor: "#EFEFEE",
        color: "black",
        paddingLeft: "3%",
        paddingRight: "3%",
        boxSizing: "border-box",
      }}
    >
      <Toolbar>
        <Grid container alignItems="center" justifyContent="space-between">
          <Grid item>
            <Typography variant="h5">
              <Link to={"/"} style={{ textDecoration: "none", color: "black" }}>
                <Typography
                  variant="title"
                  sx={{
                    fontFamily: "Space Grotesk",
                    fontSize: "1.7rem",
                    fontWeight: 700,
                  }}
                >
                  Jun
                  <Typography variant="span" sx={{ color: "#8ACB88" }}>
                    Empower
                  </Typography>
                </Typography>
              </Link>
            </Typography>
          </Grid>

          <Grid item>
            <Typography
              variant="subtitle1"
              color="black"
              sx={{ display: "flex", alignItems: "center" }}
            >
              <Avatar sx={{ marginRight: "0.6rem" }}>U</Avatar>
              <Typography
                sx={{
                  fontFamily: "Space Grotesk",
                  fontWeight: 500,
                  fontSize: "14px",
                  paddingRight: "6vh",
                }}
              >
                Hello,
                <br />
                <span style={{ fontWeight: 700, fontSize: "17px" }}>
                  My User Name
                </span>
              </Typography>

              <Link
                to={"/profile"}
                style={{
                  textDecoration: "none",
                  marginLeft: "16px",
                  color: "green",
                  fontFamily: "DM Sans, sans-serif",
                  fontSize: "20px",
                }}
              >
                Profile
              </Link>
            </Typography>
          </Grid>
        </Grid>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
