import { Typography, Grid, Button, styled, Pagination } from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { useState } from "react";
import CustomCard from "../components/CustomCard";
import RepoCard from "../components/RepoCard";
import { Link } from "react-router-dom";
import { cardData, repoData } from "../mockData/data";
import AboutApplication from "../components/AboutApp";
import SearchInput from "../components/SearchInput";

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
  const [expandedIndex, setExpandedIndex] = useState(-1);

  const handleExpandClick = (index) => {
    setExpandedIndex((prevIndex) => (prevIndex === index ? -1 : index));
  };

  return (
    <>
      <ThemeProvider theme={theme}>
        <Grid container spacing={1} sx={{ px: "5%", pt: "3%" }}>
          <AboutApplication />
          <Grid item xs={4}>
            <Typography variant="h6" sx={{ fontSize: "14px", mb: "2vh" }}>
              New Repo
            </Typography>

            {cardData.map((data, index) => (
              <CustomCard
                key={index}
                iconBackground={data.iconBackground}
                title={data.title}
                description={data.description}
                stars={data.stars}
                expanded={expandedIndex === index}
                handleExpandClick={() => handleExpandClick(index)}
              />
            ))}
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
          <SearchInput label="Search your repository" />

          <Grid item xs={3} sx={{ display: "flex", alignItems: "center" }}>
            <Button
              variant="contained"
              fullWidth
              sx={{ fontFamily: "Space Grotesk", fontWeight: 700 }}
            >
              <Link
                to="/add-repo"
                style={{ textDecoration: "none", color: "#000000" }}
              >
                Add your repo
              </Link>
            </Button>
          </Grid>
        </Grid>

        <Grid item xs={12} sx={{ px: "5%", pb: "5%" }}>
          <GridStyle container spacing={5} sx={{ mb: "0" }}>
            {repoData.map((data, index) => (
              <Grid item xs={12} sm={6} md={4} key={index}>
                <RepoCard img={data.img} name={data.name} desc={data.desc} />
              </Grid>
            ))}
          </GridStyle>
        </Grid>
        <Grid
          item
          xs={12}
          container
          justifyContent="center"
          alignItems="center"
          sx={{ px: "5%", pb: "3%" }}
        >
          <Pagination count={10} color="primary" />
        </Grid>
      </ThemeProvider>
    </>
  );
};

export default Home;
