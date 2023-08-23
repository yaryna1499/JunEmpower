import RequireAuth from "../router/RequireAuth";
import Navbar from "./Navbar/Navbar";
import { Box } from "@mui/material";

const AuthenticatedLayout = ({ children }) => (
  <RequireAuth>
    <Navbar />
    <Box paddingTop="3rem">{children}</Box>
  </RequireAuth>
);

export default AuthenticatedLayout;
