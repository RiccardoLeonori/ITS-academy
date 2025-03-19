'''Esercizio 9
Il valore di π può essere approssimato utilizzando la seguente serie infinita:
π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari 
per ottenere approssimazioni sempre più accurate.

Quindi:
progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''


den: int = 3
c: int = 1    # contatore dei termini della serie (inizializzato a 1 considerando il primo termine uguale a 4)
threshold: float = 0.00001
pi: float = 4.0
targets_list: list[float] = [3.14, 3.141, 3.1415, 3.14159]
slicing = 4

# calcola la serie finchè non sono stati raggiunti (e rimossi) tutti i valori target
while targets_list:
    
    c += 1

    if c % 2 == 0:
        pi -= 4/den
    else:
        pi += 4/den

    den += 2
    
    # se la differenze tra pi e il target è compresa tra + e - threshold (0.00001) la considero un'approssimazione accurata, la stampo e rimuovo il target della lista
    if str(pi)[:slicing] == str(targets_list[0]):

        print(f"Siamo al {c}° termine della serie e abbiamo ottenuto un'approssimazione accurata di {targets_list[0]} --> {pi}")
        slicing += 1
        targets_list.pop(0)