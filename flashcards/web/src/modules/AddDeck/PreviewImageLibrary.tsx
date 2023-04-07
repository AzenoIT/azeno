import { CircularProgress, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { faker } from "@faker-js/faker";
import { Image } from "./ImagePicker";

interface LibraryImageListProps {
    setShowModal: (showModal: boolean) => void;
    images: Image["images"];
    setIsLoading: (isLoading: boolean) => void;
    isLoading: boolean;
}

function PreviewImageLibrary({ images, isLoading, setIsLoading, setShowModal }: LibraryImageListProps) {
    const [previewImages, setPreviewImages] = useState<string[]>([]);

    useEffect(() => {
        const fetchImages = async () => {
            try {
                const fakerImages = Array.from({ length: 3 }).map(() => {
                    return faker.image.technics(300, 200, true);
                });
                console.log(fakerImages);
                setPreviewImages(fakerImages);
            } catch (error) {
                console.error("Error fetching images:", error);
            }
        };

        fetchImages();
    }, []);

    const handleShowModal = () => {
        setIsLoading(true);
        setTimeout(() => {
            setShowModal(true);
            setIsLoading(false);
        }, 1000);
    };

    return (
        <div
            onClick={handleShowModal}
            style={{
                position: "relative",
                display: "flex",
                maxWidth: "600px",
                margin: "auto",
                borderRadius: "25px",
                overflow: "hidden",
                cursor: "pointer",
            }}
        >
            {previewImages.map((image) => (
                <div
                    key={image}
                    style={{
                        backgroundImage: `url(${image})`,
                        backgroundPosition: "center",
                        backgroundRepeat: "no-repeat",
                        backgroundSize: "cover",
                        position: "relative",
                        maxWidth: "200px",
                        width: "100%",
                        height: "164px",
                    }}
                />
            ))}
            <div
                style={{
                    backgroundColor: "rgba(0, 0, 0, 0.5)",
                    position: "absolute",
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                }}
            >
                {isLoading ? (
                    <CircularProgress color="warning" />
                ) : (
                    <Typography variant="h6" component="h2" sx={{ color: "white", position: "absolute" }}>
                        Przeglądaj obrazy
                    </Typography>
                )}
            </div>
        </div>
    );
}

export default PreviewImageLibrary;
