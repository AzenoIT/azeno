export interface FlashcardTypes {
    id: number;
    decks: number[];
    question?: string;
    questionImage?: string;
    answer?: string;
    answerImage?: string;
}

const flashcardsData = [
    {
        id: 1,
        decks: [1, 2],
        question: "Test question 1",
        answerImage: "https://loremflickr.com/cache/resized/65535_52577433028_03981836de_c_640_480_nofilter.jpg",
    },
    {
        id: 2,
        decks: [3, 4],
        question: "Test question 2",
        answer: "Test answer 2",
    },
    {
        id: 3,
        decks: [1, 3],
        questionImage: "https://loremflickr.com/cache/resized/65535_52747902192_11973635d9_c_640_480_nofilter.jpg",
        answerImage: "https://loremflickr.com/cache/resized/65535_52577178555_f38ed21c3e_b_640_480_nofilter.jpg",
    },
    {
        id: 4,
        decks: [1, 4],
        questionImage: "https://loremflickr.com/cache/resized/65535_52653192095_42870b0ee6_c_640_480_nofilter.jpg",
        answer: "Test answer 4",
    },
    {
        id: 5,
        decks: [2, 3],
        question: " Test question 5",
        answer: "Test answer 5",
    },
    {
        id: 6,
        decks: [1, 4],
        question: "Test question 6",
        answer: "Test answer 6",
    },
    {
        id: 6,
        decks: [2, 3],
        question: "Test question 7",
        answer: "Test answer 7",
    },
    {
        id: 7,
        decks: [2, 4],
        questionImage: "https://loremflickr.com/cache/resized/65535_52747902192_11973635d9_c_640_480_nofilter.jpg",
        answerImage: "https://loremflickr.com/cache/resized/65535_52577178555_f38ed21c3e_b_640_480_nofilter.jpg",
    },
    {
        id: 9,
        decks: [1, 4],
        question: "Test question 9",
        answer: "Test answer 9",
    },
    {
        id: 10,
        decks: [1, 2],
        question: "Test question 10",
        answer: "Test answer 10",
    },
];

export default flashcardsData;
