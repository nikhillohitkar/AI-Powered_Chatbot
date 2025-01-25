import React, { useState } from "react";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { setMessage } from "../redux/actions";
import { TextField, Button, Box, Typography } from "@mui/material";

const Chatbot = () => {
    const [query, setQuery] = useState("");
    const messages = useSelector((state) => state.messages);
    const dispatch = useDispatch();

    const handleQuerySubmit = async () => {
        if (!query) return;

        // Dispatch user message to state
        dispatch(setMessage({ user: query, bot: "" }));

        try {
            const response = await axios.post("http://localhost:8000/query/", {
                user_query: query,
            });
            dispatch(setMessage({ user: query, bot: response.data.response }));
            setQuery(""); // Clear input
        } catch (error) {
            console.error("Error:", error);
        }
    };

    return (
        <Box sx={{ width: 400, padding: 2 }}>
            <Typography variant="h5" gutterBottom>
                Chatbot
            </Typography>
            {messages.map((message, index) => (
                <Box key={index} sx={{ marginBottom: 2 }}>
                    <Typography><strong>User:</strong> {message.user}</Typography>
                    <Typography><strong>Bot:</strong> {message.bot}</Typography>
                </Box>
            ))}
            <TextField
                label="Ask me anything about products or suppliers"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                fullWidth
            />
            <Button onClick={handleQuerySubmit} variant="contained" sx={{ marginTop: 2 }}>
                Ask
            </Button>
        </Box>
    );
};

export default Chatbot;
