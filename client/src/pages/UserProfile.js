import * as React from 'react';
import { useState } from 'react';
import DriveFileRenameOutlineIcon from '@mui/icons-material/DriveFileRenameOutline';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { 
  Avatar,
  Button,
  CssBaseline,
  Box,
  Typography,
  Tab,
  List,
  Link,
  Divider, 
  ListItem, 
  ListItemText,
} from '@mui/material';
import {
  TabContext,
  TabList,
  TabPanel,
} from '@mui/lab';


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
          main: "#FFFFFF",
        },
        secondary: {
          main: "#EEEEEF",
          light: '#f5f5f5',
          contrastText: '#bdbdbd',
        },
      },
});

export default function UserProfile() {
  const [value, setValue] = useState("1");
  const handleChange = (e, newValue) => {
    setValue(newValue);
  }

  return (
    <ThemeProvider theme={theme}>
        <CssBaseline />
        <Box
          sx={{
            backgroundColor: '#E0C591',
            padding: "2rem",
            paddingTop: "4rem",
            borderRadius: "1rem",
            minHeight: "calc(100vh - var(--navbar-height))",
          }}
        >
                <Box sx={{
                    display: "flex",
                    flexWrap: "wrap",
                    gap: 4,
                    alignItems: "flex-start",
                    justifyContent: "center"
                    
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
                        <Button
                          type="submit"
                          fullWidth
                          variant="contained"
                          sx={{ mt: 3, mb: 2, fontFamily: "DM Sans", fontWeight: 700, textTransform: "none" }}
                          >
                          Edit profile <DriveFileRenameOutlineIcon sx={{ml: 2}} />
                      </Button>
                    </Box>
                    <Box sx={{maxWidth: "900px", width: "100%"}}>
                      <TabContext 
                      value={value}
                      >
                        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                          <TabList 
                          onChange={handleChange} 
                          aria-label="lab API tabs example"
                          centered
                          >
                            <Tab label="About me" value="1" />
                            <Tab label="Skills" value="2" />
                            <Tab label="Projects" value="3" />
                          </TabList>
                        </Box>
                        <TabPanel value="1">
                          Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolor quisquam assumenda eaque. Distinctio iste officia sapiente suscipit iure. Dolorem, nostrum.
                          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aut doloribus molestiae, repudiandae non nulla deserunt minima eaque quam possimus incidunt porro excepturi numquam culpa doloremque maiores sequi voluptates at iure deleniti quaerat nobis quae magnam. In laudantium aliquam necessitatibus nisi. Libero reprehenderit quam dolores dicta dolorum accusantium beatae repellendus explicabo.
                        </TabPanel>
                        <TabPanel value="2">
                          <List>
                            <ListItem>
                              <ListItemText primary='Coding languages:' secondary=' Python, HTML5, JavaScript, CSS, PHP, SQL, C++, Ruby, .NET.' />
                            </ListItem>
                            <Divider />
                            <ListItem>
                              <ListItemText primary='Operating systems:' secondary=' Linux, Windows, masOS, Android, iOS.' />
                            </ListItem>
                            <Divider />
                            <ListItem>
                              <ListItemText primary='Cloud computing:' secondary=' Azure, AWS, Google Cloud, Amazon Web, Kamatera, Oracle.' />
                            </ListItem>
                            <Divider />
                            <ListItem>
                              <ListItemText primary='eCommerce Platforms:' secondary='Shopify, WooCommerce, BigCommerce, Magento, OpenCart.' />
                            </ListItem>
                            <Divider />
                            <ListItem>
                              <ListItemText primary='Network security:' secondary='Cloud security, malware analysis, intrusion detection, CEH, OSCP, CISA, GCIH, secude code development, data and file encryption.' />
                            </ListItem>
                            <Divider />
                            <ListItem>
                              <ListItemText primary='Data analysis:' secondary='OLAP, data queries, data cube technology, raw data processing and integration, data structures and algorithms, Tableau.' />
                            </ListItem>
                            <Divider />
                            <ListItem>
                              <ListItemText primary=' AI:' secondary='machine learning, natural language processing, AI integration and application.' />
                            </ListItem>
                            <Divider />
                            <ListItem>
                              <ListItemText primary='Application and desktop software development:' secondary='Android/iOS Software Development Kit, Android/iOS UX and UI, SQL, Xcode development, Github, React.js, Angular.' />
                            </ListItem>
                            <Divider />
                          </List>
                        </TabPanel>
                        <TabPanel value="3">
                          <List>
                            <ListItem>
                              <ListItemText 
                                primary={<Link href="#" sx={{textDecoration: "none", color: "inherit", "&:hover": {textDecoration: "underline", color: "#FFFFFF"}}}>JunEmpower</Link>} 
                                secondary='A platform for young IT professionals to showcase their work, get feedback and interact with employers.' />
                            </ListItem>
                            <Divider />
                            <ListItem>
                              <ListItemText primary={<Link href="#" sx={{textDecoration: "none", color: "inherit", "&:hover": {textDecoration: "underline", color: "#FFFFFF"}}}>Lorem</Link>}  secondary='Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolor quisquam assumenda eaque. Distinctio iste officia sapiente suscipit iure. Dolorem, nostrum.' />
                            </ListItem>
                          </List>
                        </TabPanel>
                      </TabContext>
                    </Box>
                </Box>
            </Box>
    </ThemeProvider>
  );
}