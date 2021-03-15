import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';
import recipesReducer from '../features/recipes/recipesSlice';

export default configureStore({
  reducer: {
    counter: counterReducer,
    recipes: recipesReducer,
  },
});
