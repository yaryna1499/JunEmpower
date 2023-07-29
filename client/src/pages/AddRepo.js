import * as React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { 
    Avatar,
    Button,
    CssBaseline,
    TextField,
    Grid,
    Box,
    Typography,
  } from '@mui/material';


const theme = createTheme({
    typography:{
        title: { 
            fontFamily: "DM Sans", 
            fontSize: "1rem", 
            fontWeight: 700,
            marginBottom: "1rem"
        },
        text:{
            fontSize: "0.8rem",
            fontWeight: 400,
            marginBottom: "0"
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

export default function AddRepo() {
  const handleSubmit = (event) => {
    event.preventDefault();
  };

  return (
    <ThemeProvider theme={theme}>
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: "center",
            alignItems: 'center',
            backgroundColor: '#F5F9FB',
            padding: "2rem",
            borderRadius: "1rem",
          }}
        >
            <Box sx={{padding: "1rem"}}>
                <Typography component="h4" variant="title" sx={{mb: 3}}>
                    Add Your Repo
                </Typography>
                <Box sx={{
                    display: "flex",
                    flexDirection: "row",
                    gap: 1.5,
                    alignItems: "center"
                }}>
                    <Avatar alt="Remy Sharp" src="/images/avatar/1.jpg" sx={{ width: 56, height: 56 }} />
                    <Box>
                        <Typography component="h5" variant="title" sx={{mb: 0}}>
                            Remy Sharp
                        </Typography>
                        <Typography component="p" variant="text">
                            Accra, GHA
                        </Typography>
                    </Box>
                </Box>
                <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
                    <Grid container>
                    <Grid item xs={12}>
                        <Typography component="h5" variant="title">
                            Repo Name
                        </Typography>
                        <TextField
                        autoComplete="given-name"
                        name="repoName"
                        fullWidth
                        id="repoName"
                        label="Write the title of your repo here"
                        sx={{mb: 3, backgroundColor: "#ffffff", boxShadow: "0 0 10px 0 #AAA6B9", borderRadius: "4px"}}
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <Typography component="h5" variant="title">
                            GitHub Link
                        </Typography>
                        <TextField
                        autoComplete="given-name"
                        name="githubLink"
                        fullWidth
                        id="githubLink"
                        label="Write the title of your post here"
                        sx={{mb: 3, backgroundColor: "#ffffff", boxShadow: "0 0 10px 0 #AAA6B9", borderRadius: "4px"}}
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <Typography component="h5" variant="title">
                            Description
                        </Typography>
                        <TextField
                        autoComplete="given-name"
                        name="description"
                        fullWidth
                        id="description"
                        label="Write about your project"
                        multiline
                        rows={4}
                        sx={{mb: 3, backgroundColor: "#ffffff", boxShadow: "0 0 10px 0 #AAA6B9", borderRadius: "4px"}}
                        />
                    </Grid>
                    </Grid>
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2, fontFamily: "Space Grotesk", fontWeight: 700 }}
                        >
                        Add Repo
                    </Button>
                </Box>
            </Box>
        </Box>
    </ThemeProvider>
  );
}