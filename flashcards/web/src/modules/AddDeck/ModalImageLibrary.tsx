import { useState } from "react";
import { Grid, Box, IconButton, Typography } from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import { Image } from "./ImagePicker";

interface ModalImageLibraryProps {
    images: Image["images"];
    handleImageSelect: (image: string | null) => void;
    closeLibrary: () => void;
}

function ModalImageLibrary({ images, handleImageSelect, closeLibrary }: ModalImageLibraryProps) {
    const [clickedImage, setClickedImage] = useState<string | null>(null);

    const handleImageClick = (image: string) => {
        setClickedImage(image);
    };

    return (
        <Box
            sx={{
                position: "fixed",
                top: 0,
                left: 0,
                width: "100%",
                height: "100%",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                background: "rgba(0, 0, 0, 0.5)",
            }}
            onClick={closeLibrary}
        >
            <Box
                sx={{
                    position: "relative",
                    width: "100%",
                    maxWidth: "800px",
                    backgroundColor: "#29455B",
                    borderRadius: "25px",
                    padding: "16px",
                    cursor: "default",
                }}
                onClick={(e) => e.stopPropagation()}
            >
                <Grid container spacing={1}>
                    {images.map((item) => (
                        <Grid item xs={12} sm={6} md={4} key={item}>
                            <button
                                type="button"
                                onClick={() => handleImageClick(item)}
                                style={{
                                    border: "none",
                                    background: "none",
                                    padding: 0,
                                    margin: 0,
                                    cursor: "pointer",
                                    outline: "none",
                                }}
                            >
                                <img
                                    src={item}
                                    alt={item}
                                    style={{
                                        width: "100%",
                                        borderRadius: "15px",
                                        border: clickedImage === item ? "4px solid #FBB916" : "4px solid #19344A",
                                        boxSizing: "border-box",
                                        transition: "0.3s",
                                    }}
                                    onMouseEnter={(e) => {
                                        if (clickedImage !== item) {
                                            e.currentTarget.style.border = "4px solid #CAA815";
                                        }
                                    }}
                                    onMouseLeave={(e) => {
                                        if (clickedImage !== item) {
                                            e.currentTarget.style.border = "4px solid #19344A";
                                        }
                                    }}
                                />
                            </button>
                        </Grid>
                    ))}
                </Grid>
                <IconButton
                    sx={{
                        position: "absolute",
                        top: "-16px",
                        right: "-16px",
                        background: "#FDFEFD",
                        color: "black",
                        "&:hover": {
                            background: "#e0e0e0",
                        },
                    }}
                    onClick={closeLibrary}
                >
                    <CloseIcon />
                </IconButton>
                {clickedImage && (
                    <button
                        type="button"
                        onClick={() => handleImageSelect(clickedImage)}
                        style={{
                            position: "absolute",
                            bottom: "8px",
                            right: "8px",
                            background: "#FAA815",
                            color: "white",
                            borderRadius: "25px",
                            border: "none",
                            padding: "8px 16px",
                            cursor: "pointer",
                            fontSize: "16px",
                            opacity: "0.9",
                            transition: "0.3s",
                        }}
                        onMouseEnter={(e) => {
                            e.currentTarget.style.opacity = "1";
                        }}
                        onMouseLeave={(e) => {
                            e.currentTarget.style.opacity = "0.9";
                        }}
                    >
                        {/* Przycisk wybierz zamknięty w tagy typography, style bold */}
                        <Typography
                            variant="h6"
                            component="h2"
                            sx={{ color: "white", position: "relative", fontWeight: "bold" }}
                        >
                            Wybierz
                        </Typography>
                    </button>
                )}
            </Box>
        </Box>
    );
}

export default ModalImageLibrary;
