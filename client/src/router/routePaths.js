export const BASE_APP_PATH = "/";

const route = (routePath) => `${BASE_APP_PATH}${routePath}`;

export const routePaths = {
  base: route(""),
  signin: route("signin"),
  signup: route("signup"),

  profile: route("profile"),
  addRepo: route("add-repo"),
};

