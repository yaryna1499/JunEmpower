import RequireAuth from "../router/RequireAuth";
import Navbar from "./Navbar";

const AuthenticatedLayout = ({ children }) => (
  <RequireAuth>
    <Navbar />
    {children}
  </RequireAuth>
);

export default AuthenticatedLayout;
