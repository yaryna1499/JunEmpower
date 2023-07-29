import React from "react";
import {
  Avatar,
  Card,
  CardContent,
  CardHeader,
  Divider,
  IconButton,
  Typography,
} from "@mui/material";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import StarIcon from "@mui/icons-material/Star";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

const CustomCard = ({
  iconBackground,
  title,
  description,
  stars,
  expanded,
  handleExpandClick,
}) => {
  return (
    <Card sx={{ mt: "1rem", mb: "1rem" }}>
      <CardHeader
        avatar={
          <Avatar
            sx={{ bgcolor: iconBackground }}
            aria-label="recipe"
          >
            {title.charAt(0)}
          </Avatar>
        }
        action={
          <IconButton aria-label="settings">
            <MoreVertIcon />
          </IconButton>
        }
        title={title}
      />
      <Divider />
      <CardContent>
        <Typography variant="body2" fontSize="16px">
          {description}
        </Typography>
      </CardContent>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "end",
          padding: "0.5rem",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "end",
          }}
        >
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
        </div>
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
