#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

# create arr for recipe and arr for ingredients

  recipe_keys = [*recipe]
  ingredients_keys = [*ingredients]

# create var to skip for loop if we don't have all the ingredients

  skip = False

# need to make sure ingredients contains all keys from recipe, else return 0

  if len(ingredients_keys) < len(recipe_keys):
    skip = True

# will need a batches variable

  batches = 100000 # set to infinity so that first remainder will always be less
  
# loop over ingredients and divide (//) each value in ingredients by its relative in recipe

  for i in range(0, len(recipe)):

    # check skip var
    if skip == True:
      batches = 0
    # if any result == 0, return 0
    elif ingredients[ingredients_keys[i]] // recipe[recipe_keys[i]] < batches:
      batches = ingredients[ingredients_keys[i]] // recipe[recipe_keys[i]]


# lowest remainder from the group is the # of batches
  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))