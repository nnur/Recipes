import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchRecipes = createAsyncThunk(
    'recipes/fetchRecipes',
    async () => {
      const apiPort = process.env.REACT_APP_API_PORT;
      const apiUrl = process.env.REACT_APP_API_URL;
      console.log(`${apiUrl}:${apiPort}`)
      const response = await axios.get(`${apiUrl}:${apiPort}/recipes`)
      return response.data
    }
)
export const recipesSlice = createSlice({
  name: 'recipes',
  initialState: {
    recipes: [],
  },
  reducers: {},
  extraReducers: {
      [fetchRecipes.fulfilled]: (state, action) => {
        state.recipes = action.payload;
        console.log("Babaoo");
      }
  }
});

export const selectRecipes = state => state.recipes.recipes;

export default recipesSlice.reducer;
