'''
8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.'''

# si, ho seguito le linee guida

def make_car(manufacturer, model_name, **kwargs) ->str:
    dic = {"manufacturer" : manufacturer, "model_name" : model_name}
    for key,value in kwargs.items():
        dic[key] = value
    return dic

car = make_car("subaru", "outback", color = "blue", tow_package = True)
print(car)

# esempio di esercizio usando le linee guida di pep8