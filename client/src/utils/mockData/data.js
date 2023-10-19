import icon2 from "../../assets/icons8-react-native-48.png";
import icon3 from "../../assets/icons8-material-ui-48.png";
import icon4 from "../../assets/icons8-redux-48.png";
import repoImg from "../../assets/Best Practices For eCommerce Website Design.png";
import img1 from "../../assets/2023-06-12 23_17_23-Menu _ Pizzeria.png";
import img2 from "../../assets/cardimg1.jpg";
import img3 from "../../assets/photo_2023-07-29_20-55-16.jpg";
import img4 from "../../assets/2023-07-29 21_41_06-Vite App.png";

export const icons = [
  { id: 1, src: icon2, alt: "Icon 2" },
  { id: 2, src: icon3, alt: "Icon 3" },
  { id: 3, src: icon4, alt: "Icon 4" },
];

export const cardData = [
  {
    iconBackground: "green",
    title: "Front-end Project 1",
    description: "Description of Front-end Project 1...",
    stars: 10,
  },
  {
    iconBackground: "blue",
    title: "Front-end Project 2",
    description: "Description of Front-end Project 2...",
    stars: 5,
  },
];

export const repoData = [
  {
    img: img1,
    name: "La Pizzeria",
    desc: "HTML5, CSS, JSON, RestApi, JS.",
  },
  {
    img: img2,
    name: "Multi-page site",
    desc: "Layout on pug, scss",
  },
  {
    img: img3,
    name: "Travel blog",
    desc: "Graphql, Gatsby",
  },
  {
    img: img4,
    name: "Weather App",
    desc: "A sleek and user-friendly weather app that provides real-time weather updates and forecasts for any location worldwide.",
  },
  {
    img: repoImg,
    name: "My project",
    desc: "This is a description",
  },
  {
    img: repoImg,
    name: "My project",
    desc: "This is a description",
  },
  {
    img: repoImg,
    name: "My project",
    desc: "This is a description",
  },
];
