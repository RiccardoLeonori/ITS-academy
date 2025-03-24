'''
1. Write a new class called Food, it should have name, price and
description as attributes.
2. Instantiate at least three different foods you know and like.
3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])
4. Create a addFood() and removeFood() for the Menu
5. Create a few new Food instances. Add each to the Menu using the respective
Method.
6. Add a method printPrices() that list all items on the Menu with their
prices.
7. Add a Menu method getAveragePrice() that returns the average Food
price of the Menu'''

class Food:

    def __init__(self, name:str, price:float, description:str):
        self.name = name
        self.price = price
        self.description = description

class Menu:

    def __init__(self, Food = []):
        self.food_list = Food

    def addFood(self, food:Food):
        self.food_list.append(food)

    def removeFood(self, food:Food):
        if food in self.food_list:
            self.food_list.remove(food)

    def  printPrices(self):
        for food in self.food_list:
            print(f"{food.name} : {food.price}")
        
    def getAveragePrice(self):
        media = 0.0
        for food in self.food_list:
            media += food.price
        return media/len(self.food_list)
            
        

pasta = Food("Pasta", 10.00, "A plate of pasta")
pizza = Food("Pizza", 10.00, "A circle pizza")
rice = Food("Rise", 5.00, "white")

sushi = Food("Sushi", 20.00, "Raw fish")
menu = Menu()

menu.addFood(sushi)
menu.printPrices()
print(menu.getAveragePrice)
print(menu.food_list)