import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect
} from "react-router-dom";
import { Counter } from './features/counter/Counter';
import { Recipes } from './features/recipes/Recipes';
import { RecipeDetail } from './features/recipe-detail/RecipeDetail';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route
            exact
            path="/"
            render={() => (
              <React.Fragment>
                <Counter />
                <Recipes />
              </React.Fragment>
            )}
          />
          <Route exact path="/recipes/:recipeId" component={RecipeDetail} />
          <Redirect to="/" />
        </Switch>
      </div>
    </Router>
  )
}

export default App;
