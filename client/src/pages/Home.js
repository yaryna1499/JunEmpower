import { Typography, Grid } from "@mui/material";
import React from "react";
import { useState } from "react";
import CustomCard from "../components/CustomCard";
import Slider from "../components/Slider";

const Home = () => {
  const [expanded, setExpanded] = useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
  return (
    <Grid container spacing={1} sx={{ px: "5%", pt: "3%" }}>
      <Grid item xs={8}>
        <Typography variant="h4">About our Application:</Typography>
        <Typography variant="h5" sx={{ mt: "0.5rem", maxWidth: "70%" }}>
          Empowering young IT professionals with a platform to showcase their
          work, receive valuable feedback, and connect with potential employers.
          Join our community and take your career to new heights!
        </Typography>

        <Slider />
      </Grid>

      <Grid item xs={4} spacing={1}>
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
  );
};

export default Home;
