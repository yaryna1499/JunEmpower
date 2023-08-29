import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Profile from "../pages/UserProfile";
import NotFound from "../pages/NotFound";
import Home from "../pages/Home";
import AddRepo from "../pages/AddRepo";
import MainLayout from "../layout/MainLayout";

import ProtectedRoute from "./ProtectedRoute";
import { ThemeProvider } from "@mui/material";
import { authTheme } from "../utils/theme/theme";
import { routePaths } from "./routePaths";

import SignUp from "../pages/authPage/SignUp";
import SignIn from "../pages/authPage/SignIn";

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
        path: routePaths.signin,
        element: (
          <ThemeProvider theme={authTheme}>
            <SignIn />
          </ThemeProvider>
        ),
      },
      {
        path: routePaths.signup,
        element: (
          <ThemeProvider theme={authTheme}>
            <SignUp />
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
