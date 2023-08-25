import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Profile from "../pages/UserProfile";
import NotFound from "../pages/NotFound";
import Home from "../pages/Home";
import AddRepo from "../pages/AddRepo";
import MainLayout from "../layout/MainLayout";

import ProtectedRoute from "./ProtectedRoute";
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
      <MainLayout>
        <NotFound />
      </MainLayout>
    ),
    children: [
      {
        index: true,
        element: (
          <MainLayout>
            <Home />
          </MainLayout>
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
          <ProtectedRoute>
            <Profile />
          </ProtectedRoute>
        ),
      },
      {
        path: routePaths.addRepo,
        element: (
          <ProtectedRoute>
            <AddRepo />
          </ProtectedRoute>
        ),
      },
    ],
  },
]);
