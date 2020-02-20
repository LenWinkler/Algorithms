#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

# create arr for recipe and arr for ingredients
  recipe_keys = recipe.keys()
  ingredients_keys = ingredients.keys()
  print(recipe_keys)
  print(ingredients_keys)

# need to make sure ingredients contains all keys from recipe, else return 0

  if len(ingredients_keys) < len(recipe_keys):
    batches = 0
  
# loop over ingredients using if <ingredient from recipe> in ingredients: continue, else: return 0
# will need a batch variable
  batches = 0
# divide each key in ingredients by its relative in recipe
# if any result == 0, return 0
# lowest remainder from the group is the # of batches

  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))