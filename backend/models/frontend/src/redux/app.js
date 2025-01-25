import React from 'react';
import Chatbot from './components/Chatbot';
import { Provider } from 'react-redux';
import store from './redux/store';

const App = () => {
    return (
        <Provider store={store}>
            <Chatbot />
        </Provider>
    );
};

export default App;
