import React from "react";
import { Formik, Form, Field } from "formik";
import { TextField, Button } from "@mui/material";
import { registrationValidationSchema } from "../../utils/schemas/authSchemas";

const RegistrationForm = ({ handleSubmit }) => {
  const initialValues = {
    email: "",
    password: "",
    username: "",
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={registrationValidationSchema}
      onSubmit={handleSubmit}
    >
      {({ errors, touched, isSubmitting }) => (
        <Form>
          <Field
            name="username"
            as={TextField}
            variant="standard"
            margin="normal"
            label="Username"
            autoComplete="username"
            fullWidth
            error={Boolean(touched.username && errors.username)}
            helperText={touched.username && errors.username}
          />
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
            autoComplete="new-password"
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
            Sign Up
          </Button>
        </Form>
      )}
    </Formik>
  );
};

export default RegistrationForm;
