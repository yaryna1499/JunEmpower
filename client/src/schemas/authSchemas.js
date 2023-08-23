import * as Yup from "yup";

export const loginValidationSchema = Yup.object({
  email: Yup.string()
    .email("Invalid email format")
    .required("This field is required"),
  password: Yup.string().required("This field is required"),
});

export const registrationValidationSchema = Yup.object({
  email: Yup.string()
    .email("Invalid email format")
    .required("This field is required"),
  password: Yup.string().required("This field is required"),
  username: Yup.string().required("This field is required"),
});
