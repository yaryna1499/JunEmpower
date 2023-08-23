import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Profile from "../pages/UserProfile";
import NotFound from "../pages/NotFound";
import Home from "../pages/Home";
import AddRepo from "../pages/AddRepo";
import LayoutWithNavbar from "../layout/LayoutWithNavbar";

import AuthenticatedLayout from "../layout/AuthenticatedLayout";
import LoginPage from "../pages/authPage/Login";
import RegistrationPage from "../pages/authPage/SignUp";
import { ThemeProvider } from "@mui/material";
import { authTheme } from "../utils/theme/theme";
import { routePaths } from "./routePaths";

export const routes = createBrowserRouter([
  {
    path: routePaths.base,
    element: <App />,
    errorElement: (
      <LayoutWithNavbar>
        <NotFound />
      </LayoutWithNavbar>
    ),
    children: [
      {
        index: true,
        element: (
          <LayoutWithNavbar>
            <Home />
          </LayoutWithNavbar>
        ),
      },

      // Public routes
      {
        path: routePaths.login,
        element: (
          <ThemeProvider theme={authTheme}>
            <LoginPage />
          </ThemeProvider>
        ),
      },
      {
        path: routePaths.signup,
        element: (
          <ThemeProvider theme={authTheme}>
            <RegistrationPage />
          </ThemeProvider>
        ),
      },

      // Private routes
      {
        path: routePaths.profile,
        element: (
          <AuthenticatedLayout>
            <Profile />
          </AuthenticatedLayout>
        ),
      },
      {
        path: routePaths.addRepo,
        element: (
          <AuthenticatedLayout>
            <AddRepo />
          </AuthenticatedLayout>
        ),
      },
    ],
  },
]);
