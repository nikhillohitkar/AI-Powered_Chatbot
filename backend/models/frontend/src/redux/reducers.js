const initialState = {
    messages: [],
};

export const chatbotReducer = (state = initialState, action) => {
    switch (action.type) {
        case "SET_MESSAGE":
            return {
                ...state,
                messages: [...state.messages, action.payload],
            };
        default:
            return state;
    }
};
