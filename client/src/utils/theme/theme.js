import { createTheme } from "@mui/material";

export const authTheme = createTheme({
  typography: {
    title: {
      fontSize: 32,
      fontWeight: "600",
      fontFamily: "Kodchasan, sans-serif",
    },
  },
  palette: {
    primary: {
      main: "#00204A",
    },
    secondary: {
      main: "#EEEEEF",
    },
  },
});
