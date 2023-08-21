import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Profile from "../pages/UserProfile";
import NotFound from "../pages/NotFound";
import Home from "../pages/Home";
import AddRepo from "../pages/AddRepo";
import LayoutWithNavbar from "../layout/LayoutWithNavbar";

import Login from "../pages/Login";
import Register from "../pages/Register";
import { ErrorPage } from "../error.page";
import AuthenticatedLayout from "../layout/AuthenticatedLayout";


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
