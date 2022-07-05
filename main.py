from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
import random as rand
import scraping as scr #webscraping file
import math

#############
# This was made for personal use
# It is very roughly made as I did not have time for great optimizations & fancy things
# There are a number of issues to fix and handy extensions
# but the main idea is to just facilitate life a little bit at home
# even if it's with a pretty ugly excel spreadsheet
#############

#############
# Improvements:
# - scrape only the number of recipes desired
# - create ingredient list taking into consideration quantities and duplicates (pretty hard)
# - create an interface that isn't the terminal
# - allow meal planning to happen with recipes from multiple bbc goodfood pages
# - there's a bug with the number of meals, can't plan 14 meals if dinner only or lunch only
# - also a bug with number of recipes on webpage; does not check whether nr of meals > nr of recipes on page
# among others...
#############



def main():
    url = ''
    number_meals = 0
    lunch, dinner = True, True
    while (True): # wait for valid input
        print("--------")
        print("Please enter a valid BBC goodfood URL\n")
        input_url = input()

        # make sure there are no weird whitespaces
        if ' ' in input_url:
            print("Your url is", input_url)
            print("Error: You have whitespace(s) your URL")
            print("Please enter a valid URL without whitespace(s)")
            continue

        # must be from bbc goodfood
        elif ("https://www.bbcgoodfood.com/recipes" not in input_url):
            print("You entered", input_url)
            print("Error: needs to be a BBC goodfood recipe list link beginning with 'https://www.bbcgoodfood.com/recipes' ")

        else:
            url = input_url
            break

    while (True):
        print("\n How many meals do you want me to plan using this page?\n")
        nr = input()
        nr = int(nr)

        if nr > 14:
            print("I don't want to plan meals for more than a week at a time :(")
            print("Please enter a number less than or equal to 14")
            continue

        else:
            number_meals = nr
            break

    while (True):
        print("\n Would you like me to plan both lunch and dinner?\n")
        print("Reply with D for dinner, L for lunch or D L for both.")
        reply = input()

        if reply == "D":
            dinner = True
            lunch = False
            break

        elif reply == "L":
            lunch = True
            dinner = False
            break

        elif reply == "D L" or reply == "DL":
            # they're both true by default so we just move on
            break

        else:
            print("Error: invalid input")
            continue



    if url == '':
        print("Something went very wrong and now you have no URL")
        return

    recipes = scr.scrape(input_url)
    # using number_meals

    # randomize list of recipes in-place
    print("Shuffling your recipes..")
    rand.shuffle(recipes)


    # work only with desired nr of recipes
    desired_recipes = recipes[:number_meals]
    weekdays = ["Mon", "Tues", "Wedn", "Thurs", "Fri", "Sat", "Sun"]
    cols = weekdays[:math.ceil(len(desired_recipes)/2)]
    lunch_recipes = []
    dinner_recipes = []
    lunch_names = []
    dinner_names = []

    print("Generating your spreadsheet...")

    if (dinner and not lunch):
        # we only need one row filled in this case
        dinner_recipes = desired_recipes
        lunch_names = ['' for m in dinner_recipes]
        dinner_names = [rcp.name for rcp in dinner_recipes]
        cols = weekdays[:len(dinner_names)]

    elif (lunch and not dinner):
        lunch_recipes = desired_recipes
        dinner_names = ['' for m in lunch_recipes]
        lunch_names = [rcp.name for rcp in lunch_recipes]
        cols = weekdays[:len(lunch_names)]

    else: # we have both so we split it
        index = math.floor(len(desired_recipes)/2)
        lunch_recipes = desired_recipes[index:]
        dinner_recipes = desired_recipes[:index]
        lunch_names = [rcp.name for rcp in lunch_recipes]
        dinner_names = [rcp.name for rcp in dinner_recipes]
        if len(lunch_names) > len(dinner_names):
            dinner_names.append(" ")
        elif len(dinner_names) > len(lunch_names):
            lunch_names.append(" ")


    # create dataframe to use in excel sheet
    df = pd.DataFrame([lunch_names, dinner_names],
                  index=["Lunch", "Dinner"], columns = cols )

    # it's not the most beautiful excel sheet, but it does the job
    df.to_excel('my_meal_plan.xlsx')
    print("Your excel sheet is ready!")

    # recipe list, mainly for ingredients (like a shopping list)
    print("Writing your ingredient list...")
    ingredients = open("ingredients_by_recipe.txt", "w")
    for recipe in desired_recipes:
        ingredients.write(recipe.name + "\n")
        ingredients.write("url: {} \n\n".format(recipe.url))
        for ing in recipe.ingredients:
            ingredients.write(ing + "\n")
        ingredients.write("------" + "\n")
    print("Your ingredient list is ready!")
    print("The files can be found in the same directory as the python files")









if __name__ == "__main__":
    main()
