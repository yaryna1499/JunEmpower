import { Typography, Grid } from "@mui/material";
import Slider from "./Slider";

const AboutApplication = () => {
  return (
    <Grid item xs={8}>
      <Typography variant="h4">About our Application:</Typography>
      <Typography variant="h5" sx={{ mt: "0.5rem", maxWidth: "70%" }}>
        Empowering young IT professionals with a platform to showcase their
        work, receive valuable feedback, and connect with potential employers.
        Join our community and take your career to new heights!
      </Typography>
      <Slider />
    </Grid>
  );
};

export default AboutApplication;
