import { createStore } from 'redux';
import { chatbotReducer } from './reducers';

const store = createStore(chatbotReducer);
export default store;
