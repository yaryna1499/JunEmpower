import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import Container from '@mui/material/Container';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import IconButton from '@mui/material/IconButton';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import HomeIcon from '@mui/icons-material/Home';
import CommentIcon from '@mui/icons-material/Comment';
import ReplyIcon from '@mui/icons-material/Reply';
import SettingsIcon from '@mui/icons-material/Settings';
import Fab from '@mui/material/Fab';
import { createTheme, ThemeProvider } from '@mui/material/styles';


const theme = createTheme({
    typography:{
        title: { 
            fontFamily: "DM Sans", 
            fontSize: "2rem", 
            fontWeight: 700,
            marginBottom: "1rem"
        },
        text:{
            fontSize: "1.2rem",
            fontWeight: 400,
            marginBottom: "0",
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

export default function UserProfile() {

  return (
    <ThemeProvider theme={theme}>
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            // alignItems: 'flex-end',
            backgroundColor: '#E0C591',
            padding: "2rem",
            borderRadius: "1rem",
          }}
        >
                <Box sx={{
                    display: "flex",
                    
                }}>
                    <Box sx={{
                      display: "flex",
                      flexDirection: "column",
                      alignItems: "center",
                      justifyContent: "center",
                      gap: 1.5,

                    }}>
                    <Avatar alt="Remy Sharp" src="/images/avatar/1.jpg" sx={{ width: 300, height: 300 }} />
                        <Typography component="h5" variant="title" sx={{mb: 0}}>
                            Remy Sharp
                        </Typography>
                        <Typography component="p" variant="text">
                            Accra, GHA
                        </Typography>
                    </Box>
                </Box>
                <TabContext 
                // value={value}
                >
                  <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                    <TabList 
                    // onChange={handleChange} 
                    aria-label="lab API tabs example">
                      <Tab label="About me" value="1" />
                      <Tab label="Skills" value="2" />
                      <Tab label="Projects" value="3" />
                    </TabList>
                  </Box>
                  <TabPanel value="1">
                    
                  </TabPanel>
                  <TabPanel value="2">Item Two</TabPanel>
                  <TabPanel value="3">Item Three</TabPanel>
                </TabContext>
            </Box>
    </ThemeProvider>
  );
}