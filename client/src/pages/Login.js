import * as React from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Link from '@mui/material/Link';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import ButtonGroup from '@mui/material/ButtonGroup';
import FormControl from '@mui/material/FormControl';
import RadioGroup from '@mui/material/RadioGroup';
import Radio from '@mui/material/Radio';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';


const theme = createTheme({
    typography:{
        title: { 
            fontFamily: "Space Grotesk", 
            fontSize: "3rem", 
            fontWeight: 700
        },
        span:{
            color: "#8ACB88",
        }
    },
    palette: {
        primary: {
          main: "#FFBF46",
        },
        secondary: {
          main: "#EEEEEF",
          light: '#f5f5f5',
          contrastText: '#bdbdbd',
        },
      },
});

export default function Login() {

    const initialValues = {
        email: '',
        password: '',
      };
    
      const validationSchema = Yup.object({
        email: Yup.string().email('Невірний формат електронної пошти').required('Обов\'язкове поле'),
        password: Yup.string().required('Обов\'язкове поле'),
      });
    

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
              marginTop: 8,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
        >
          <Typography component="h1" variant="title" sx={{mb: 3}}>
            Jun<Typography variant="span">Empower</Typography>
          </Typography>
          <ButtonGroup
            disableElevation
            variant="contained"
            aria-label="Disabled elevation buttons"
            sx={{width: "100%"}}
            >
                <Button color="secondary" sx={{width: "50%", fontFamily: "Space Grotesk", fontWeight: 700, borderRight: "none"}}>Register</Button>
                <Button sx={{width: "50%", fontFamily: "Space Grotesk", fontWeight: 700}}>Login</Button>
            </ButtonGroup>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
                {() => (
                    <Form>
                    <Field
                        name="email"
                        as={TextField}
                        variant="standard"
                        margin="normal"
                        required
                        label="Email Address"
                        type="email"
                        fullWidth
                        id="email"
                        autoComplete="email"
                        autoFocus

                        //     error={Boolean(touched.email && errors.email)}
                    //     helperText={touched.email && errors.email}
                    />
                    <Field
                        name="password"
                        as={TextField}
                        variant="standard"
                        margin="normal"
                        required
                        label="Password"
                        type="password"
                        fullWidth
                        id="password"
                        autoComplete="current-password"
                        // error={Boolean(touched.password && errors.password)}
                        // helperText={touched.password && errors.password}
                    />
                        <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2, fontFamily: "Space Grotesk", fontWeight: 700 }}
                        >
                        Sign In
                        </Button>
                    </Form>
                )}
                </Formik>
                <FormControl>
                  <RadioGroup
                    aria-labelledby="demo-controlled-radio-buttons-group"
                    name="controlled-radio-buttons-group"
                    // value={value}
                    // onChange={handleChange}
                  >
                    <FormControlLabel value="developer" control={<Radio />} label="Remember me as developer" />
                    <FormControlLabel value="company" control={<Radio />} label="Remember me as company" />
                  </RadioGroup>
                </FormControl>
            <Box sx={{
                fontFamily: "Space Grotesk", 
                fontWeight: 700,
                fontSize: "1.2rem",
                marginTop: 8,
                }}>
                <Box>
                    Forgot password? 
                    <Link href="#" variant="body2" sx={{textDecoration: "none", pl: 1.5, fontSize: "1.2rem", color: "#007AFF", "&:hover": {textDecoration: "underline"}}}>
                        Remember
                    </Link>
                </Box>
                <Box>
                Don't have an account?
                    <Link href="#" variant="body2" sx={{textDecoration: "none", pl: 1.5, fontSize: "1.2rem", color: "#007AFF", "&:hover": {textDecoration: "underline"}}}>
                    {"Sign Up"}
                    </Link>

                </Box>
            </Box>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
