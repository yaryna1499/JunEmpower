import { createTheme } from "@mui/material";

export const authTheme = createTheme({
  typography: {
    title: {
      fontFamily: "Space Grotesk",
      fontSize: "3rem",
      fontWeight: 700,
    },
  },
  palette: {
    primary: {
      main: "#FFBF46",
    },
    secondary: {
      main: "#EEEEEF",
    },
  },
});

