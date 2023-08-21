import RequireAuth from "../router/RequireAuth";
import LayoutWithNavbar from "../layout/LayoutWithNavbar";

const AuthenticatedLayout = ({ children }) => (
  <RequireAuth>
    <LayoutWithNavbar>{children}</LayoutWithNavbar>
  </RequireAuth>
);

export default AuthenticatedLayout;
