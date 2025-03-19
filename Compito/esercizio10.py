'''Esercizio 10
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall'utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l'inserimento quando l'utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.'''

numeri = []
pari = []
dispari = []
frequenze = {}

# loop infinito fino all'inserimento di 0
while True:
    num = int(input("Inserisci un numero intero (0 per terminare): "))
    if num == 0:
        break
    numeri.append(num)
    
    # calcolo i numeri pari e dispari
    if num % 2 == 0:
        pari.append(num)
    else:
        dispari.append(num)
    
    # frequenza dei numeri
    if num in frequenze:
        frequenze[num] += 1
    else:
        frequenze[num] = 1

# somma dei numeri pari
somma_pari = sum(pari)
print(f"La somma dei numeri pari è: {somma_pari}")

# media dei numeri dispari
if len(dispari) > 0:
    media_dispari = sum(dispari) / len(dispari)
    print(f"La media dei numeri dispari è: {media_dispari}")
else:
    print("Non ci sono numeri dispari per calcolare la media.")

# determino il numero con la frequenza più alta
max_frequenza = max(frequenze.values())
numeri_frequenza_massima = [num for num, freq in frequenze.items() if freq == max_frequenza]

print(f"I numeri con la frequenza più alta sono: {numeri_frequenza_massima}")
