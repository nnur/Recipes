import React from 'react';
import { Counter } from './features/counter/Counter';
import { Recipes } from './features/recipes/Recipes';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        
        <Counter />
        <Recipes />
        
      </header>
    </div>
  );
}

export default App;
