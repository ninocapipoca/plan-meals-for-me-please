from bs4 import BeautifulSoup
import requests
import recipe_class as rpc

#html_text = requests.get('https://www.bbcgoodfood.com/recipes/collection/healthy-dinner-recipes').text


def scrape(url, maxnr):
    # extract recipes and turn them into objects to store the info
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    # get recipe cards
    print("finding recipes..")
    recipes = soup.find_all('li', class_= 'dynamic-list__list-item list-item', limit=maxnr)

    recipe_objects = []
    for recipe in recipes:
        title = recipe.find('h2', class_ = "heading-4").text
        link = recipe.find('a', class_ = "link d-block", href = True)
        next_url = 'https://www.bbcgoodfood.com/recipes' + link['href']

        recipe_text = requests.get(next_url).text
        recipe_soup = BeautifulSoup(recipe_text, 'lxml')
        ingredients = recipe_soup.find_all('li', class_ = "pb-xxs pt-xxs list-item list-item--separator")

        ingredientlist = [ing.text for ing in ingredients]
        recipe_objects.append(rpc.Recipe(title, ingredientlist, next_url))

    if len(recipe_objects) == 0:
        print("Oops, no recipes found")
        print(recipe_objects)
        return

    return recipe_objects
