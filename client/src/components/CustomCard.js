import React from "react";
import {
  Avatar,
  Card,
  CardContent,
  CardHeader,
  Divider,
  IconButton,
  Typography,
  Button,
  Box,
} from "@mui/material";
import StarIcon from "@mui/icons-material/Star";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import icon from "../assets/github.png";
import { icons } from "../utils/mockData/data";

const CustomCard = ({
  iconBackground,
  title,
  description,
  stars,
  expanded,
  handleExpandClick,
}) => {
  return (
    <Card sx={{ mt: "1rem", mb: "2rem" }}>
      <CardHeader
        avatar={
          <Avatar
            sx={{ bgcolor: iconBackground, fontSize: "10px" }}
            aria-label="recipe"
          >
            Avatar
          </Avatar>
        }
        title={
          <Typography
            variant="h5"
            sx={{
              fontSize: "1.2rem",
              fontWeight: "bold",
              fontFamily: "Space Grotesk",
            }}
          >
            {title}
          </Typography>
        }
        action={
          <Box display="flex">
            {icons.map((icon) => (
              <Avatar
                key={icon.id}
                src={icon.src}
                alt={icon.alt}
                sx={{ width: 30, height: 30, marginRight: "10px" }}
              />
            ))}
          </Box>
        }
      />
      <Divider />
      <CardContent>
        <Typography variant="body2" fontSize="16px">
          {description}
        </Typography>
      </CardContent>

      <div
        style={{
          width: "100%",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <Button
          size="small"
          style={{
            color: "rgb(102, 101, 101)",
            backgroundColor: "#FFBF46",
            marginLeft: "4%",
          }}
        >
          GitHub Link
          <img
            src={icon}
            alt="GitHub Icon"
            style={{ marginLeft: "0.5rem", width: "1.2rem" }}
          />
        </Button>

        <Box>
          <IconButton aria-label="add to favorites">
            <Typography variant="h6">20</Typography>
            <StarIcon sx={{ color: "orange" }} />
          </IconButton>
          <IconButton
            onClick={handleExpandClick}
            aria-expanded={expanded}
            aria-label="show more"
          >
            <ExpandMoreIcon />
          </IconButton>
        </Box>
      </div>
      {expanded && (
        <CardContent>
          <Typography paragraph>
            Here must be a description of the project.
          </Typography>
        </CardContent>
      )}
    </Card>
  );
};

export default CustomCard;
