import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchRecipes, selectRecipes } from './recipesSlice'
import { Link } from "react-router-dom";

export function Recipes() {
    const recipes = useSelector(selectRecipes);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(fetchRecipes());
    }, [])

    console.log("rendering..")
    return (
        <div>
            <h1>
                Recipes

            </h1>

            <ul>
                {recipes.map(el => (
                    <li key={el.id}>
                        <Link to={`/recipes/${el.id}`}>
                            {el.name}
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}
