class Recipe:
    def __init__(self, _name, _ingredients, _url):
        self.name = _name
        self.ingredients = _ingredients
        self.url = _url


    def printrecipe(self):
        print(self.name)
        print(self.ingredients)
        print(self.url)
