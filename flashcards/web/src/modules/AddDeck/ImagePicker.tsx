import { Container, styled } from "@mui/material";
import { useEffect, useState } from "react";
import { faker } from "@faker-js/faker";
import PreviewImageLibrary from "./PreviewImageLibrary";
import ModalImageLibrary from "./ModalImageLibrary";

const StyledInput = styled("div")({
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    width: "100%",
    height: "164px",
    backgroundColor: "#2c3e5080",
    borderRadius: "15px",
    marginTop: "1rem",
    cursor: "pointer",
    transition: "all .3s ease-in-out",
    "&:hover": {
        backgroundColor: "#2c3e50b0",
    },
});

const ImagePickerIcon = styled("div")({
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    width: "48px",
    height: "48px",
    borderRadius: "50%",
    backgroundColor: "#FFFFFF",
    color: "#2D4E9D",
    fontSize: "2rem",
    transition: "all .3s ease-in-out",
    marginBottom: "0.5rem",
    "&:hover": {
        transform: "scale(1.1)",
    },
});

const ImagePickerText = styled("div")({
    color: "#FFFFFF",
    fontSize: "1.25rem",
    textAlign: "center",
    marginBottom: "1rem",
    transition: "all .3s ease-in-out",
});

interface ImagePickerProps {
    setSelectedImage: (image: string | null) => void;
}

export type Image = {
    images: string[];
};

function ImagePicker({ setSelectedImage }: ImagePickerProps) {
    const [showModal, setShowModal] = useState<boolean>(false);
    const [images, setImages] = useState<string[]>([]);
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [isDragging, setIsDragging] = useState<boolean>(false);

    // Funkcja obsługująca ustawienie wybranego obrazka z biblioteki
    const handleImageSelect = (image: string | null) => {
        setSelectedImage(image);
        setShowModal(false);
    };

    // Pobieranie obrazów z serwera, tymczasowo używając biblioteki faker
    useEffect(() => {
        const fetchImages = async () => {
            try {
                setIsLoading(true);
                // Tworzenie tymczasowej tablicy obrazów za pomocą biblioteki faker
                const fakerImages = Array.from({ length: 10 }).map(() => faker.image.technics(300, 200, true));
                setImages(fakerImages);
            } catch (error) {
                console.error("Error fetching images:", error);
            } finally {
                setIsLoading(false);
            }
        };

        fetchImages();
    }, []);

    const isImageValid = (file: File): boolean => {
        // Sprawdź rozszerzenie pliku
        const validImageExtensions = ["image/jpeg", "image/png"];
        if (!validImageExtensions.includes(file.type)) {
            alert("Niewłaściwy format obrazka! Obsługiwane formaty to: JPEG i PNG");
            return false;
        }

        // Sprawdź wielkość pliku (ograniczenie do 5 MB)
        const maxFileSize = 5 * 1024 * 1024; // 5 MB
        if (file.size > maxFileSize) {
            alert("Plik jest zbyt duży! Maksymalny rozmiar pliku to 5 MB.");
            return false;
        }

        return true;
    };
    const handleImageDrop = (e: React.DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        setIsDragging(false);
        const image = e.dataTransfer.files[0];

        if (image && isImageValid(image)) {
            const reader = new FileReader();

            reader.onload = () => {
                setSelectedImage(reader.result as string);
            };

            reader.readAsDataURL(image);
        }
    };

    const handleDragEnter = (e: React.DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        setIsDragging(true);
    };

    const handleDragLeave = (e: React.DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        setIsDragging(false);
    };

    const handleImageInputClick = () => {
        // Tworzenie ukrytego elementu input do wyboru plików
        const fileInput = document.createElement("input");
        fileInput.type = "file";
        fileInput.accept = "image/jpeg, image/png";

        // Obsługa zdarzenia zmiany (wyboru pliku) w elemencie input
        fileInput.onchange = (event) => {
            // Rzutowanie event.target na HTMLInputElement, aby uzyskać dostęp do właściwości files
            const target = event.target as HTMLInputElement;

            // Sprawdzanie, czy istnieje plik i czy istnieje więcej niż jeden plik
            const { files } = target;

            if (!files || files.length === 0) {
                return;
            }

            // Jeśli obraz jest prawidłowy, wczytujemy go jako DataURL
            const image = files[0];
            if (isImageValid(image)) {
                const reader = new FileReader();
                reader.onload = () => {
                    setSelectedImage(reader.result as string);
                };
                reader.readAsDataURL(image);
            }
        };

        // Wywołanie kliknięcia na ukrytym elemencie input, aby otworzyć okno wyboru plików
        fileInput.click();
    };

    return (
        <Container>
            <h2 style={{ fontSize: "1.5rem", color: "white", textAlign: "center", marginBottom: "1rem" }}>
                Wybierz obrazek (opcjonalne)
            </h2>
            <StyledInput
                style={{
                    maxWidth: "600px",
                    margin: "auto",
                    marginBottom: "1rem",
                    backgroundColor: isDragging ? "#2c3e50c0" : undefined, // Zmień backgroundColor, gdy obrazek jest przeciągany
                }}
                onDrop={handleImageDrop}
                onDragOver={(e) => e.preventDefault()}
                onDragEnter={handleDragEnter}
                onDragLeave={handleDragLeave}
                onClick={handleImageInputClick}
            >
                <ImagePickerIcon className="image-picker-icon">+</ImagePickerIcon>
                <ImagePickerText className="image-picker-text">Kliknij lub przeciągnij i upuść</ImagePickerText>
            </StyledInput>

            {/* Wybór obrazka z biblioteki */}
            <PreviewImageLibrary
                images={images}
                isLoading={isLoading}
                setIsLoading={setIsLoading}
                setShowModal={setShowModal}
            />
            {/* Wyświetlanie modalu z biblioteką obrazów */}
            {showModal && (
                <ModalImageLibrary
                    images={images}
                    handleImageSelect={handleImageSelect}
                    closeLibrary={() => setShowModal(false)}
                />
            )}
        </Container>
    );
}

export default ImagePicker;
