import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Profile from "../pages/UserProfile";
import NotFound from "../pages/NotFound";
import Home from "../pages/Home";
import AddRepo from "../pages/AddRepo";
import RequireAuth from "./RequireAuth";
import PrivateLayout from "../layout/PrivateLayout";

import Login from "../pages/Login";
import Register from "../pages/Register";

export const routes = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: (
          <RequireAuth>
            <PrivateLayout>
              <Home />
            </PrivateLayout>
          </RequireAuth>
        ),
      },
      {
        path: "profile",
        element: (
          <RequireAuth>
            <PrivateLayout>
              <Profile />
            </PrivateLayout>
          </RequireAuth>
        ),
      },
      {
        path: "add-repo",
        element: (
          <RequireAuth>
            <PrivateLayout>
              <AddRepo />
            </PrivateLayout>
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
        path: "addrepo",
        element: <AddRepo />,
      },
      {
        path: "*",
        element: (
          <PrivateLayout>
            <NotFound />
          </PrivateLayout>
        ),
      },
    ],
  },
]);
