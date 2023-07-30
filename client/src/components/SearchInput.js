import React from "react";
import { Grid, TextField } from "@mui/material";

const SearchInput = ({ label}) => {
  return (
    <Grid
      item
      xs={4}
      sx={{ display: "flex", alignItems: "center", position: "relative" }}
    >
      <TextField
        name="repoName"
        fullWidth
        id="repoName"
        label={ label}
        autoFocus
        sx={{
          mb: 3,
          backgroundColor: "#ffffff",
          boxShadow: "0 0 10px 0 #AAA6B9",
          borderRadius: "4px",
        }}
      />
    </Grid>
  );
};

export default SearchInput;
