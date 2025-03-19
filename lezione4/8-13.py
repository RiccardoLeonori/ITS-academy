'''
8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'''

def build_profile(name, last_name,**kwargs) ->str:
    dic = {}
    string:str = f"{name} {last_name}"
    for key,value in kwargs.items():
        dic[key] = value
    for key,value in dic.items():
        string += f"{key} {value}, "
    return (string[:-2])

name = "Riccardo"
last_name = "Leonori"
dic = build_profile(name, last_name, age = 19, hair = "brown", weight = 169)
print(dic)