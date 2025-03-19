'''
Let's try to define a function named subtract ourselves:
● It should take 2 parameters.
● Inside the function, it should subtract the two.
● Then, return the result.
After you defined it, call the function with some arguments!'''

def subtract(n1, n2):
    x = n1 - n2
    return x

n1 = int(input("Scrivi il primo numero: "))
n2 = int(input("Scrivi il secondo numero: "))
print(f"La differenza tra il primo e il secondo numero è: {subtract(n1, n2)}")