'''Esercizio 6
Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, 
e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.
Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

# chiedo all'utente di inserire dei numeri interi n1 e n2
n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

prodotto = 1

# determino l'intervallo da considerare
inizio = min(n1, n2)
fine = max(n1, n2)

# calcolo del prodotto dei numeri compresi tra inizio e fine, inclusi
for i in range(inizio, fine + 1):
    prodotto *= i

# eseguo il print dell'output
print(f"Il prodotto di tutti i numeri tra {n1} e {n2} è: {prodotto}")
