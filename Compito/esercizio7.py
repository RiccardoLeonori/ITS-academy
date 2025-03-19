'''Esercizio 7
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, 
entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.'''

a = []
b = []
somma_incrociata = 0

# numeri per la lista a
n = int(input("Inserisci il numero di elementi nelle liste: "))
for i in range(n):
    a.append(int(input(f"Inserisci il numero per la lista a: ")))

# numeri per la lista b
for i in range(n):
    b.append(int(input(f"Inserisci il numero per la lista b: ")))

# calcolo della somma incrociata
for i in range(n):
    somma_incrociata += a[i] + b[i]

# eseguo il print dell'output
print(f"La somma incrociata degli elementi è: {somma_incrociata}")
