import { useEffect, useState } from "react";
import { IconButton, styled } from "@mui/material";
import { NavigateBefore, NavigateNext } from "@mui/icons-material";
import slider1 from "../assets/christopher-gower-m_HRfLhgABo-unsplash.jpg";
import { Box } from "@mui/material";

const sliderArray = [
  { image: slider1 },
  { image: slider1 },
  { image: slider1 },
];

const StyledIconButton = styled(IconButton)(({ theme }) => ({
  position: "absolute",
  top: "50%",
  transform: "translateY(-50%)",
  backgroundColor: "white",
  transition: "background-color 0.3s ease",
  "&:hover": {
    backgroundColor: "rgba(255, 255, 255, 0.8)",
  },
}));

export const SliderContainer = styled(Box)(({ theme }) => ({
  position: "relative",
  height: "53vh",
}));

export const SlideImage = styled("img")(({ theme }) => ({
  width: "100%",
  height: "100%",
  objectFit: "cover",
  transition: "opacity 0.3s linear 2s,",
}));

const Slider = () => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [imageLoaded, setImageLoaded] = useState(false);
  const currentSlide = sliderArray[currentImageIndex];

  const handlePreviousImage = () => {
    setCurrentImageIndex((prevIndex) =>
      prevIndex === 0 ? sliderArray.length - 1 : prevIndex - 1
    );
  };

  const handleNextImage = () => {
    setCurrentImageIndex((prevIndex) =>
      prevIndex === sliderArray.length - 1 ? 0 : prevIndex + 1
    );
  };

  useEffect(() => {
    const image = new Image();
    image.src = currentSlide.image;
    image.onload = () => {
      setImageLoaded(true);
    };
  }, [currentSlide.image]);

  useEffect(() => {
    const interval = setInterval(handleNextImage, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <>
      {imageLoaded && (
        <SliderContainer sx={{mt: "5vh", maxWidth: "95%"}}>
          <SlideImage src={currentSlide.image} alt="slider" />

          <StyledIconButton style={{ left: 0, marginLeft: "5%" }}>
            <NavigateBefore onClick={handlePreviousImage} />
          </StyledIconButton>

          <StyledIconButton style={{ right: 0, marginRight: "5%", mt: "1%" }}>
            <NavigateNext onClick={handleNextImage} />
          </StyledIconButton>
        </SliderContainer>
      )}
    </>
  );
};

export default Slider;
