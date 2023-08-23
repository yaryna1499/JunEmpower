import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Profile from "../pages/UserProfile";
import NotFound from "../pages/NotFound";
import Home from "../pages/Home";
import AddRepo from "../pages/AddRepo";
import LayoutWithNavbar from "../layout/LayoutWithNavbar";

import { ErrorPage } from "../error.page";
import AuthenticatedLayout from "../layout/AuthenticatedLayout";
import LoginPage from "../pages/Login";
import RegistrationPage from "../pages/Register";
import { ThemeProvider } from "@mui/material";
import { authTheme } from "../theme/theme";

export const routes = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        index: true,
        element: (
          <LayoutWithNavbar>
            <Home />
          </LayoutWithNavbar>
        ),
      },
      {
        path: "profile",
        element: (
          <AuthenticatedLayout>
            <Profile />
          </AuthenticatedLayout>
        ),
      },
      {
        path: "add-repo",
        element: (
          <AuthenticatedLayout>
            <AddRepo />
          </AuthenticatedLayout>
        ),
      },
      {
        path: "login",
        element: (
          <ThemeProvider theme={authTheme}>
            <LoginPage />
          </ThemeProvider>
        ),
      },
      {
        path: "register",
        element: (
          <ThemeProvider theme={authTheme}>
            <RegistrationPage />
          </ThemeProvider>
        ),
      },
      {
        path: "*",
        element: (
          <LayoutWithNavbar>
            <NotFound />
          </LayoutWithNavbar>
        ),
      },
    ],
  },
]);
