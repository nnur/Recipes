import React from 'react'
import { selectRecipes } from './../recipes/recipesSlice'
import { useSelector } from 'react-redux'

export const RecipeDetail = ({ match }) => {
  const { recipeId } = match.params
  const recipe = useSelector(state => {
    return selectRecipes(state).find(recipe => recipe.id === recipeId)
  })

  console.log("rendering detail")

  if (!recipe) {
    return (
      <section>
        <h2>recipe not found!</h2>
      </section>
    )
  }

  return (
    <section>
      <article className="recipe">
        <h2>{recipe.name}</h2>
        <div> Servings: {recipe.servings}</div>
        <p className="recipe-content">{recipe.description}</p>
      </article>
    </section>
  )
}