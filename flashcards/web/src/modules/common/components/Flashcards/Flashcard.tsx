import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Container, Box } from "@mui/material";
import AnswerView from "./AnswerView";
import flashcardsData from "./flashcardsData";

function Flashcard(): JSX.Element {
    const [flashcards, setFlashcards] = useState(flashcardsData);
    const [flashcard, setFlashcard] = useState(flashcards[0]);

    const { id } = useParams();

    useEffect(() => {
        const deckId = Number(id);
        setFlashcards(flashcardsData.filter((card) => card.decks.includes(deckId)));
    }, [id]);

    // function nextFlashcard is for testing purposes only
    const nextFlashcard = () => {
        setFlashcard(flashcards[Math.floor(Math.random() * flashcards.length)]);
    };

    return (
        <Container maxWidth="lg" className="h-screen">
            <Box className="mt-20 w-full flex flex-col items-center justify-center">
                <AnswerView flashcard={flashcard} nextFlashcard={nextFlashcard} />
            </Box>
        </Container>
    );
}

export default Flashcard;
