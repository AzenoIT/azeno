import { Card, CardContent, Typography, Divider } from "@mui/material";

interface flashcardTextProps {
    question: string;
}
function FlashcardTextComponent({ question }: flashcardTextProps): JSX.Element {
    return (
        <Card
            className="flex flex-col items-center"
            sx={{
                maxWidth: 545,
                minWidth: { xs: "100%", sm: 545 },
                height: 300,
                backgroundColor: "#FFEFD6",
                borderRadius: "15px",
            }}
            elevation={3}
        >
            <CardContent className="w-full text-left">
                <Typography variant="body2">1/35</Typography>
            </CardContent>
            <Divider className="w-11/12" sx={{ borderColor: "#FDBC11" }} />
            <CardContent className="flex flex-col items-center justify-center">
                <Typography variant="body1">{question}</Typography>
            </CardContent>
        </Card>
    );
}

export default FlashcardTextComponent;
