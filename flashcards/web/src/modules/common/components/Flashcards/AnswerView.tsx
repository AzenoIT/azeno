import { MouseEventHandler } from "react";
import { Button } from "@mui/material";
import FlashcardTextComponent from "./FlashcardTextComponent";
import { FlashcardTypes } from "./flashcardsData";

interface AnswerViewProps {
    flashcard: FlashcardTypes;
    nextFlashcard: MouseEventHandler<HTMLButtonElement>;
}
function AnswerView({ flashcard, nextFlashcard }: AnswerViewProps): JSX.Element {
    return (
        <>
            {flashcard.question && <FlashcardTextComponent question={flashcard.question} />}
            <Button variant="contained" onClick={nextFlashcard}>
                Next
            </Button>
        </>
    );
}

export default AnswerView;
