export const BASE_APP_PATH = "/";

const route = (routePath) => `${BASE_APP_PATH}${routePath}`;

export const routePaths = {
  base: route(""),
  login: route("login"),
  signup: route("signup"),

  profile: route("profile"),
  addRepo: route("add-repo"),
};

