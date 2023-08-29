import {
  Dialog,
  DialogTitle,
  DialogContent,
  IconButton,
  Button,
} from "@mui/material";
import { Close as CloseIcon } from "@mui/icons-material";

const Modal = ({ isSuccessModalOpen, handleCloseModal }) => {
  return (
    <Dialog open={isSuccessModalOpen} onClose={handleCloseModal}>
      <DialogTitle>
        <IconButton
          aria-label="close"
          onClick={handleCloseModal}
          sx={{
            position: "absolute",
            right: 8,
            top: 8,
            color: (theme) => theme.palette.error.main,
          }}
        >
          <CloseIcon />
        </IconButton>
        Registration Successful
      </DialogTitle>
      <DialogContent>
        <p>Your registration was successful. Please login to continue.</p>
        <Button
          onClick={handleCloseModal}
          sx={{ backgroundColor: "#8ACB88" }}
          variant="contained"
        >
          Login
        </Button>
      </DialogContent>
    </Dialog>
  );
};

export default Modal;
