'''Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). 
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).'''

# inizializzo le variabili
numeri_interi = []
numeri = []
numero = 0

# ciclo di acquisizione dei numeri
while True:
    numero = float(input("Inserisci un numero (inseriscilo negativo per terminare): "))
    
    # se il numero è negativo esce dal ciclo
    if numero < 0:
        break
    
    # aggiungo il numero alla lista di tutti i numeri
    numeri.append(numero)
    
    # se il numero è un intero, lo aggiungo alla lista dei numeri interi
    if numero.is_integer():

        # converto a int per avere solo la parte intera
        numeri_interi.append(int(numero))

# calcolare la media dei numeri interi
if numeri_interi:
    media_interi = sum(numeri_interi) / len(numeri_interi)
    print(f"La media dei numeri interi è: {media_interi:.2f}")
else:
    print("Non sono stati inseriti numeri interi.")

# determino il numero più grande e il numero più piccolo tra tutti i numeri
if numeri:
    numero_max = max(numeri)
    numero_min = min(numeri)
    print(f"Il numero più grande inserito è: {numero_max}")
    print(f"Il numero più piccolo inserito è: {numero_min}")
else:
    print("Nessun numero valido inserito.")
