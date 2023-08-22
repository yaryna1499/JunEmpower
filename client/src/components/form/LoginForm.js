import React from "react";
import { Formik, Form, Field } from "formik";
import { TextField, Button } from "@mui/material";
import { loginValidationSchema } from "../../schemas/authSchemas";

const LoginForm = ({ handleSubmit }) => {
  const initialValues = {
    email: "",
    password: "",
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
            variant="standard"
            margin="normal"
            label="Email Address"
            type="email"
            fullWidth
            autoComplete="email"
            error={Boolean(touched.email && errors.email)}
            helperText={touched.email && errors.email}
          />
          <Field
            name="password"
            as={TextField}
            variant="standard"
            margin="normal"
            label="Password"
            type="password"
            fullWidth
            autoComplete="current-password"
            error={Boolean(touched.password && errors.password)}
            helperText={touched.password && errors.password}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            disabled={isSubmitting}
            sx={{
              mt: 3,
              mb: 2,
              fontFamily: "Space Grotesk",
              fontWeight: 700,
            }}
          >
            Sign In
          </Button>
        </Form>
      )}
    </Formik>
  );
};

export default LoginForm;
