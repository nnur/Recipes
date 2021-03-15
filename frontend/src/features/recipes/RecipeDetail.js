import React from 'react'
import { useSelector } from 'react-redux'

export const RecipeDetail = ({ match }) => {
  const { recipeId } = match.params

  const post = useSelector(state =>
    state.posts.find(recipe => recipe.id === recipeId)
  )

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
        <p className="recipe-content">{recipe.description}</p>
      </article>
    </section>
  )
}