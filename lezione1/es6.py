'''
Progetta un algoritmo per calcolare il fattoriale di un numero intero positivo fornito dall'utente.'''

while True:
    n = int(input("Scrivi il numero: "))
    if n > 0:
        break
    else:
        print("Il numero inserito deve essere positivo")
fattoriale = 1
i = 1
while True:
    if i == n:
        print(fattoriale)
        break
    else:
        fattoriale *= i
        i += 1