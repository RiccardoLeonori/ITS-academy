'''
PATH: str = "lezione15/prova.txt"
mode: str = "r"
encoding = "utf-8"

file = open(PATH)

print(file)

output: str = file.read()
print(output)
file.close()
'''

'''

        metodo giusto ma non elegante

file = open("lezione15/prova.txt", "a")
try:
    output: str = file.read()
except Exception as e:
    print(f"An error occured: {e}")
finally:
    file.close()
'''

'''
        metodo GIUSTO (si chiude da solo il file)

with open("lezione15/prova.txt", "r") as file:
    print(file.read())
'''