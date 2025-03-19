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

pi_approssimato = 0
n = 1
segno = 1
termini = 0

# Soglie di precisione richieste
soglie = [3.14, 3.141, 3.1415, 3.14159]

for x in soglie:

    # reset delle variabili per ogni soglia
    pi_approssimato = 0
    n = 1
    segno = 1
    termini = 0

    # calcolo i termini fino a raggiungere la precisione richiesta
    for i in range(10000000):
        pi_approssimato += segno * (4 / n)
        n += 2
        segno *= -1
        termini += 1

        # controllo se la differenza tra l'approssimazione e la soglia è inferiore a una piccola tolleranza
        if (pi_approssimato - x) < 0.00001 and (x - pi_approssimato) < 0.00001:
            break

    # eseguo il print dell'output
    print(f"Per ottenere π ≈ {x} sono necessari {termini} termini della serie.")
    print(f"Approssimazione ottenuta: {pi_approssimato}\n")