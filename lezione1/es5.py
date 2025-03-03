'''
Progetta un algoritmo per determinare se un numero intero positivo inserito dall'utente è un numero primo.'''

#metodo uno
n = int(input("Scrivi il numero: "))
if n < 2:
    print("Il numero non è primo")
else:
    div = 2
    while True:
        if div < n:
            if n % div == 0:
                print("Il numero non è primo")
                break
            else:
                div += 1
        else:
            print("Il numero è primo")
            break

#metodo 2
n = int(input("Scrivi il numero: "))
if n < 2:
    print("Il numero non è primo")
else:
    div = 2
    while True:
        if div <= n**0.5:
            if n % div == 0:
                print("Il numero non è primo")
                break
            else:
                div += 1
        else:
            print("Il numero è primo")
            break