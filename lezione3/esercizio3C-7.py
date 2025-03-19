'''Esercizio 3C-7. 
Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.
'''

teste = 0
croci = 0
lanci_totali = 8

for i in range(lanci_totali):
    while True:
        lancio = str(input(f"Inserisci il risultato del lancio (\"t\" per testa, \"c\" per croce): ")).lower()
        match lancio:
            case "t":
                teste += 1
                break
            case "c":
                croci += 1
                break
            case _:
                print("Input non valido. Inserisci 'T' per testa o 'C' per croce.")

percentuale_teste = (teste / lanci_totali) * 100
percentuale_croci = (croci / lanci_totali) * 100

print("\nRisultati:")
print(f"Testa: \"{teste}\" ({percentuale_teste:.2f}%)")
print(f"Croce: \"{croci}\" ({percentuale_croci:.2f}%)")