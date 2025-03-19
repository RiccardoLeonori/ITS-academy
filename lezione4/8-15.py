'''
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.'''

from esercizio14 import make_car

car = make_car("kawasaki", "ninja", color = "blue", tow_package = True)
print(car)