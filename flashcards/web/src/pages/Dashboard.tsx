import React, { useState, JSX } from "react";
import Button from "@mui/material/Button";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import InputLabel from "@mui/material/InputLabel";
import FormControl from "@mui/material/FormControl";

function Dashboard(): JSX.Element {
    const [filterDecks, setFilterDecks] = useState("all");

    const handleChange = (e) => {
        setFilterDecks(e.target.value);
    };

    type DeckJson = {
        id: number;
        title: string;
        flashcards: number;
        mastered: number;
        lastViewed: string;
        status?: string[];
        image: string;
    };

    const decksJsonServer: DeckJson[] = [
        {
            id: 1,
            title: "python advanced",
            flashcards: 26,
            mastered: 15,
            lastViewed: "2 days ago",
            status: ["all", "new"],
            image: "https://loremflickr.com/640/480/all",
        },
        {
            id: 2,
            title: "react hooks",
            flashcards: 21,
            mastered: 19,
            lastViewed: "7 days ago",
            status: ["all", "started"],
            image: "https://loremflickr.com/640/480/nature",
        },
        {
            id: 3,
            title: "react basics",
            flashcards: 28,
            mastered: 5,
            lastViewed: "32 days ago",
            status: ["all", "finished"],
            image: "https://loremflickr.com/640/480/berlin",
        },
        {
            id: 4,
            title: "python basics",
            flashcards: 30,
            mastered: 10,
            lastViewed: "2 days ago",
            status: ["all", "new"],
            image: "https://loremflickr.com/640/480/dog",
        },
        {
            id: 5,
            title: "js advanced",
            flashcards: 24,
            mastered: 24,
            lastViewed: "1 day ago",
            status: ["all", "finished"],
            image: "https://loremflickr.com/640/480/poland",
        },
        {
            id: 6,
            title: "js basics",
            flashcards: 21,
            mastered: 19,
            lastViewed: "8 days ago",
            status: ["all", "started"],
            image: "https://loremflickr.com/640/480/paris",
        },
        {
            id: 7,
            title: "django basics",
            flashcards: 25,
            mastered: 25,
            lastViewed: "15 days ago",
            status: ["all", "finished"],
            image: "https://loremflickr.com/640/480/london",
        },
        {
            id: 8,
            title: "django advanced",
            flashcards: 21,
            mastered: 19,
            lastViewed: "3 days ago",
            status: ["all", "started"],
            image: "https://loremflickr.com/640/480/girl",
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
                        {decksJsonServer
                            .filter((item) => item.status.includes(filterDecks))
                            .map((deck) => (
                                <div key={deck.title} className="bg-white p-2 rounded-md border-2 border-stone-400">
                                    <div className="bg-stone-100 w-full h-32 rounded-md">
                                        <img className="w-full h-full object-cover" src={deck.image} />
                                    </div>
                                    <div className="space-y-2 py-4">
                                        <a href="/train">
                                            <p className="text-xl pb-2">{deck.title}</p>
                                        </a>
                                        <div className="text-xs flex justify-between gap-4">
                                            <p>{deck.flashcards} flashcards</p>
                                            <p>
                                                <span className="font-bold">
                                                    {Math.round((deck.mastered / deck.flashcards) * 100)}%
                                                </span>{" "}
                                                mastered
                                            </p>
                                        </div>
                                        <p className="text-xs">
                                            {deck.lastVisited === "never"
                                                ? "Never visited"
                                                : `Last visited ${deck.lastViewed}`}
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
