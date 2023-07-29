import { Button, CardActions, Divider, Box, Typography, IconButton } from "@mui/material";
import { Link as RouteLink } from "react-router-dom";
import { Card, styled } from "@mui/material";
import img1 from "../assets/Best Practices For eCommerce Website Design.png";
import StarIcon from "@mui/icons-material/Star";
import icon from "../assets/github.png"

export const CardStyle = styled(Card)(({ theme }) => ({
  borderRadius: theme.spacing(2),
  boxShadow: `0px 0px 4px rgba(145, 158, 171, 0.24), 0px 4px 8px -4px rgba(145, 158, 171, 0.24)`,
  "&:hover": {
    boxShadow: `rgb(145 158 171 / 24%) 0px 0px 2px 0px, rgb(145 158 171 / 24%) 0px 16px 32px -4px`,
  },
}));

const RepoCard = ({ img, name, desc}) => {
  return (
    <CardStyle>
      <Box
        sx={{
          width: "100%",
          position: "relative",
          top: 0,
          minHeight: "30vh",
          height: "32vh",
        }}
        component="img"
        src={img || img1}
        alt="img-repo"
      />

      <Box sx={{ py: 2, px: 3 }}>
        <Box display="flex" justifyContent="space-between">
          <Typography variant="h5">{name || "My project"}</Typography>
          <Typography variant="h6">User Link</Typography>
        </Box>
        <Typography sx={{ mt: "2vh", minHeight: "100px" }}>
          Description: {desc || "This is a description"}
        </Typography>
        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
          sx={{
            mt: 2,
          }}
        >
          <Button
            size="small"
            style={{
              color: "rgb(102, 101, 101)",
              backgroundColor: "#FFBF46",
            }}
            component={RouteLink}
          >
            GitHub Link
            <img
              src={icon}
              alt="GitHub Icon"
              style={{ marginLeft: "0.5rem", width: "1.2rem" }}
            />
          </Button>
          <IconButton aria-label="add to favorites">
            <Typography variant="h6">20</Typography>
            <StarIcon sx={{ color: "orange" }} />
          </IconButton>
        </Box>
        <Divider />
      </Box>
      <CardActions
        style={{ display: "flex", justifyContent: "center" }}
      ></CardActions>
    </CardStyle>
  );
};

export default RepoCard;
