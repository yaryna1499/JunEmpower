import { Button } from "@mui/material";

const CustomFormButton = ({ children, ...props }) => {
  return (
    <Button
      {...props}
      sx={{
        height: "50px",
        mt: 3,
        mb: 2,
        fontWeight: "600",
        fontFamily: "Kodchasan, sans-serif",
        textTransform: "none",
        borderRadius: "15px",
        ...props.sx,
      }}
    >
      {children}
    </Button>
  );
};

export default CustomFormButton;
