import sys
import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
import random as rand
import scraping as scr #webscraping file
import math

# Improvement - checkboxes and catching errors
  
# Add some color
# to the window
sg.theme('SandyBeach')     
  
# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
    [sg.Text('Please enter your URL and select options')],
    [sg.Text('URL', size =(15, 1)), sg.InputText()],
    [sg.Text('Lunch/Dinner', size =(15, 1)), sg.InputText()],
    #[sg.Checkbox('Dinner', default=True, enable_events=True, k='-Dinner-')],
    #[sg.Checkbox('Lunch', default=True, enable_events=True, k='-Lunch-')],
    [sg.Text('Nr meals to plan', size =(15, 1)), sg.InputText()],
    [sg.Submit('Submit'), sg.Cancel('Cancel')]
]
  
window = sg.Window('Simple data entry window', layout)
event, values = window.read()

#dinner_flag = True
#lunch_flag = True
url, reply, number_meals = values[0], values[1], values[2]
print(url, number_meals)

def main():
    print("running main")
    recipes = scr.scrape(input_url, number_meals)
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
    # if event == "-Dinner-":
    #     dinner_flag = not dinner_flag
    #     print("Dinner", dinner_flag)

    # if event == "-Lunch-":
    #     lunch_flag = not lunch_flag
    #     print("Lunch:", lunch_flag)

while True:
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Test':
        main()
        break

window.close()
  
# # The input data looks like a simple list 
# # when automatic numbered
# print(event, values[0], values[1])   

# def callback_function1():
#     sg.popup('In Callback Function 1')
#     print('In the callback function 1')


# def callback_function2():
#     sg.popup('In Callback Function 2')
#     print('In the callback function 2')


# layout = [[sg.Text('Demo of Button Callbacks')],
#           [sg.Button('Button 1'), sg.Button('Button 2')]]

# window = sg.Window('Button Callback Simulation', layout)

# while True:             # Event Loop
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     elif event == 'Button 1':
#         callback_function1()        # call the "Callback" function
#     elif event == 'Button 2':
#         callback_function2()        # call the "Callback" function

# window.close()

# sg.theme('BluePurple')

# layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Show'), sg.Button('Exit')]]

# window = sg.Window('Pattern 2B', layout)

# while True:  # Event Loop
#     event, values = window.read()
#     print(event, values)
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
#     if event == 'Show':
#         # Update the "output" text element to be the value of "input" element
#         window['-OUTPUT-'].update(window['-OUTPUT-'].get()+'\n New Text append')

# window.close()
