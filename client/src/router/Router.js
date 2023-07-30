import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Profile from "../pages/UserProfile";
import NotFound from "../pages/NotFound";
import Home from "../pages/Home";
import AddRepo from "../pages/AddRepo";
import RequireAuth from "./RequireAuth";
import LayoutWithNavbar from "../layout/PrivateLayout";

import Login from "../pages/Login";
import Register from "../pages/Register";
import { ErrorPage } from "../error.page";

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
          <RequireAuth>
            <LayoutWithNavbar>
              <Profile />
            </LayoutWithNavbar>
          </RequireAuth>
        ),
      },
      {
        path: "add-repo",
        element: (
          <RequireAuth>
            <LayoutWithNavbar>
              <AddRepo />
            </LayoutWithNavbar>
          </RequireAuth>
        ),
      },
      {
        path: "login",
        element: <Login />,
      },
      {
        path: "register",
        element: <Register />,
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
