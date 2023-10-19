import React from "react";
import { Formik, Form, Field } from "formik";
import { TextField, Checkbox } from "@mui/material";
import { loginValidationSchema } from "../../utils/schemas/authSchemas";
import CustomButton from "./CustomFormBtn";
import { StyledFormControlLabel, style } from "./styleHelper";

const LoginForm = ({ handleSubmit }) => {
  const initialValues = {
    email: "",
    password: "",
    agreeToProcessing: false,
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={loginValidationSchema}
      onSubmit={handleSubmit}
    >
      {({ errors, touched, isSubmitting }) => (
        <Form>
          <Field
            name="email"
            as={TextField}
            variant="outlined"
            margin="normal"
            label="Email Address"
            type="email"
            fullWidth
            autoComplete="email"
            error={Boolean(touched.email && errors.email)}
            helperText={touched.email && errors.email}
            InputProps={style}
          />
          <Field
            name="password"
            as={TextField}
            variant="outlined"
            margin="normal"
            label="Password"
            type="password"
            fullWidth
            autoComplete="current-password"
            error={Boolean(touched.password && errors.password)}
            helperText={touched.password && errors.password}
            InputProps={style}
          />
          <StyledFormControlLabel
            sx={{ mt: "2%" }}
            control={<Checkbox name="agreeToProcessing" color="primary" />}
            label="By checking this box, you agree to our Terms of Service Privacy Policy "
          />
          <CustomButton
            type="submit"
            fullWidth
            variant="contained"
            disabled={isSubmitting}
          >
            Sign In
          </CustomButton>
        </Form>
      )}
    </Formik>
  );
};

export default LoginForm;
