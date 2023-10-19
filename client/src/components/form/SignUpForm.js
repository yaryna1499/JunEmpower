import React from "react";
import { Formik, Form, Field } from "formik";
import { TextField, Checkbox } from "@mui/material";
import { registrationValidationSchema } from "../../utils/schemas/authSchemas";
import CustomFormButton from "./CustomFormBtn";
import { StyledFormControlLabel, style } from "./styleHelper";

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
            variant="outlined"
            margin="normal"
            label="Username"
            autoComplete="username"
            fullWidth
            error={Boolean(touched.username && errors.username)}
            helperText={touched.username && errors.username}
            InputProps={style}
          />
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
            autoComplete="new-password"
            error={Boolean(touched.password && errors.password)}
            helperText={touched.password && errors.password}
            InputProps={style}
          />
          <StyledFormControlLabel
            sx={{ mt: "2%" }}
            control={<Checkbox name="agreeToProcessing" color="primary" />}
            label="By checking this box, you agree to our Terms of Service Privacy Policy "
          />
          <CustomFormButton
            type="submit"
            fullWidth
            variant="contained"
            disabled={isSubmitting}
          >
            Sign Up
          </CustomFormButton>
        </Form>
      )}
    </Formik>
  );
};

export default RegistrationForm;
