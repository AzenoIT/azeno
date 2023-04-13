import React, { FC, useState } from "react";
import Button from "@mui/material/Button";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import InputLabel from "@mui/material/InputLabel";
import FormControl from "@mui/material/FormControl";

function Dashboard(): FC {
    const [filterDecks, setFilterDecks] = useState("all");

    const handleChange = (e) => {
        setFilterDecks(e.target.value);
    };

    type Deck = {
        title: string;
        flashcards: number;
        completed: number;
        lastVisited: string;
        status?: string[];
    };

    const decksArr: Deck[] = [
        {
            title: "Tytuł 1 - bardzo długi aby sprawdzić, jak zachowuje się UI",
            flashcards: 25,
            completed: 40,
            lastVisited: "2 days ago",
            status: ["all", "new", "started"],
        },
        {
            title: "Tytuł 2",
            flashcards: 20,
            completed: 15,
            lastVisited: "5 days ago",
            status: ["all", "new", "started"],
        },
        {
            title: "Tytuł 3",
            flashcards: 30,
            completed: 63,
            lastVisited: "10 days ago",
            status: ["all", "started"],
        },
        {
            title: "Tytuł 4",
            flashcards: 28,
            completed: 50,
            lastVisited: "2 weeks ago",
            status: ["all", "started"],
        },
        {
            title: "Tytuł 5",
            flashcards: 40,
            completed: 0,
            lastVisited: "never",
            status: ["all"],
        },
        {
            title: "Tytuł 6",
            flashcards: 13,
            completed: 100,
            lastVisited: "4 weeks ago",
            status: ["all", "finished"],
        },
    ];

    return (
        <div className="min-h-screen bg-slate-100">
            <div className="container mx-auto px-4 space-y-10">
                <div className="flex justify-between">
                    <div>home</div>
                    <div>username ICON</div>
                </div>
                <div className="max-w-5xl mx-auto space-y-8">
                    <div className="max-w-xs mx-auto sm:max-w-full flex flex-col sm:flex-row gap-4 sm:gap-8 justify-center">
                        <Button variant="outlined" href="/library">
                            Library
                        </Button>
                        <Button variant="outlined" href="/statistics">
                            Statistics
                        </Button>
                        <Button variant="outlined" href="/marketplace">
                            Marketplace
                        </Button>
                    </div>
                    <div className="flex gap-8 justify-center items-center">
                        <div className="min-w-[120px]">
                            <FormControl fullWidth>
                                <InputLabel id="filter-cards">Filter decks</InputLabel>
                                <Select
                                    labelId="filter-cards"
                                    id="filter-cards"
                                    value={filterDecks}
                                    label="Filter decks"
                                    onChange={handleChange}
                                >
                                    <MenuItem value="all">All</MenuItem>
                                    <MenuItem value="new">New</MenuItem>
                                    <MenuItem value="started">Started</MenuItem>
                                    <MenuItem value="finished">Finished</MenuItem>
                                </Select>
                            </FormControl>
                        </div>
                        <a href="/add-new-deck">
                            <div className="flex gap-2 items-center">
                                <p>Add new deck</p>
                                <div className="h-4 w-4 bg-slate-800" />
                            </div>
                        </a>
                    </div>
                    <div className="pt-8 md:pt-14 grid sm:grid-cols-2 lg:grid-cols-3 gap-8">
                        {decksArr
                            .filter((item) => item.status.includes(filterDecks))
                            .map((deck) => (
                                <div key={deck.title} className="bg-white p-2 rounded-md border-2 border-stone-400">
                                    <div className="bg-stone-100 w-full h-32 rounded-md" />
                                    <div className="space-y-2 py-4">
                                        <p className="text-xl pb-2">{deck.title}</p>
                                        <div className="text-xs flex justify-between gap-4">
                                            <p>{deck.flashcards} flashcards</p>
                                            <p>
                                                <span className="font-bold">{deck.completed}%</span> mastered
                                            </p>
                                        </div>
                                        <p className="text-xs">
                                            {deck.lastVisited === "never"
                                                ? "Never visited"
                                                : `Last visited ${deck.lastVisited}`}
                                        </p>
                                    </div>
                                </div>
                            ))}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
