import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

export default function MaterialUITest() {
    const [deckName, setDeckName] = React.useState("test");

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
    };

    return (
        <>
            <Box sx={{ mt: 4, mb: 2 }}>
                <Typography variant="h4">Add Deck Test</Typography>
            </Box>
            <form onSubmit={handleSubmit}>
                <Box sx={{ mb: 2 }}>
                    <TextField
                        fullWidth
                        label="Deck Name"
                        value={deckName}
                        onChange={(event) => setDeckName(event.target.value)}
                    />
                </Box>
                <Button variant="contained" color="primary" type="submit">
                    Submit
                </Button>
            </form>
        </>
    );
}
