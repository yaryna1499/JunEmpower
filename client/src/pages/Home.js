import { Typography, Grid, Button, TextField, styled, Pagination } from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { useEffect, useState } from "react";
import CustomCard from "../components/CustomCard";
import Slider from "../components/Slider";
import RepoCard from "../components/RepoCard";
import { Link } from "react-router-dom";
import img1 from "../assets/2023-06-12 23_17_23-Menu _ Pizzeria.png";
import img2 from "../assets/cardimg1.jpg";
import img3 from "../assets/photo_2023-07-29_20-55-16.jpg";
import img4 from "../assets/2023-07-29 21_41_06-Vite App.png";
import { postUserData } from "../api/userRequest";

const userData = {
  userName: "root",
  password:"root"
};

const GridStyle = styled(Grid)(({ theme }) => ({
  marginTop: 1,
  marginBottom: theme.spacing(5),
  justifyContent: "center",
}));

const theme = createTheme({
  typography: {
    title: {
      fontFamily: "DM Sans",
      fontSize: "1rem",
      fontWeight: 700,
      marginBottom: "1rem",
    },
    text: {
      fontSize: "0.8rem",
      fontWeight: 400,
      marginBottom: "0",
    },
  },
  palette: {
    primary: {
      main: "#FFBF46",
    },
    secondary: {
      main: "#EEEEEF",
      light: "#f5f5f5",
      contrastText: "#bdbdbd",
    },
  },
});

const Home = () => {
  const [expanded, setExpanded] = useState(false);

  // useEffect(() => {
  //   postUserData(userData);
  // }, [])

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
  return (
    <>
      <ThemeProvider theme={theme}>
        <Grid container spacing={1} sx={{ px: "5%", pt: "3%" }}>
          <Grid item xs={8}>
            <Typography variant="h4">About our Application:</Typography>
            <Typography variant="h5" sx={{ mt: "0.5rem", maxWidth: "70%" }}>
              Empowering young IT professionals with a platform to showcase
              their work, receive valuable feedback, and connect with potential
              employers. Join our community and take your career to new heights!
            </Typography>

            <Slider />
          </Grid>

          <Grid item xs={4}>
            <Typography variant="h6" sx={{ fontSize: "14px", mb: "2vh" }}>
              New Repo
            </Typography>
            <CustomCard
              iconBackground="green"
              title="Front-end Project"
              description="Description of the Front-end Project..."
              stars={10}
              expanded={expanded}
              handleExpandClick={handleExpandClick}
            />
            <CustomCard
              iconBackground="green"
              title="Front-end Project"
              description="Description of the Front-end Project..."
              stars={10}
              expanded={expanded}
              handleExpandClick={handleExpandClick}
            />
          </Grid>
        </Grid>

        <Grid item xs={14} sx={{ pt: "5vh", px: "5vw", pb: "3vh" }}>
          <Typography variant="h4" sx={{ fontSize: "23px" }}>
            All repositories:
          </Typography>
        </Grid>

        <Grid
          container
          spacing={2}
          sx={{
            px: "5%",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <Grid
            item
            xs={4}
            sx={{ display: "flex", alignItems: "center", position: "relative" }}
          >
            <TextField
              name="repoName"
              fullWidth
              id="repoName"
              label="Search your repository"
              autoFocus
              sx={{
                mb: 3,
                backgroundColor: "#ffffff",
                boxShadow: "0 0 10px 0 #AAA6B9",
                borderRadius: "4px",
              }}
            />
          </Grid>

          <Grid item xs={3} sx={{ display: "flex", alignItems: "center" }}>
            <Button variant="contained" fullWidth sx={{fontFamily: "Space Grotesk", fontWeight: 700}}>
              <Link
                to="/add-repo"
                style={{ textDecoration: "none", color: "#000000"}}
              >
                Add your repo
              </Link>
            </Button>
          </Grid>
        </Grid>

        <Grid item xs={12} sx={{ px: "5%", pb: "5%" }}>
          <GridStyle container spacing={5} sx={{ mb: "0" }}>
            <Grid item xs={12} sm={6} md={4}>
              <RepoCard
                img={img1}
                name="La Pizzeria"
                desc="HTML5, CSS, JSON, RestApi, JS."
              />
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <RepoCard
                img={img2}
                name="Multi-page site"
                desc="Layout on pug, scss"
              />
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <RepoCard img={img3} name="Travel blog" desc="Graphql, Gatsby" />
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <RepoCard
                img={img4}
                name="Weather App"
                desc="A sleek and user-friendly 
                weather app that provides real-time
                 weather updates and forecasts for any location worldwide."
              />
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <RepoCard />
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <RepoCard />
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <RepoCard />
            </Grid>
          </GridStyle>
        </Grid>
        <Grid item xs={12} container justifyContent="center" alignItems="center" sx={{ px: "5%", pb: "3%" }}>
          <Pagination count={10} color="primary" />
        </Grid>
      </ThemeProvider>
    </>
  );
};

export default Home;
