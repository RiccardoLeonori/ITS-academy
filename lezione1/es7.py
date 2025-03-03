'''
Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari.'''

pari = 0
dispari = 0
cont = 0

while cont < 10:
    n = int(input("Scrivi il numero: "))
    if n % 2 == 0:
        pari += 1
    else:
        dispari += 1
    cont +=1
print(f"I numeri pari sono {pari}")
print(f"I numeri dispari sono {dispari}")