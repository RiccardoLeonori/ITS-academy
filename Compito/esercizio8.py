'''Esercizio 8
Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) 
e visualizzi in output un grafico a barre testuale con asterischi *.
Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.'''

numeri = []

# prendo in input 5 interi
for i in range(5):
    while True:
        num = int(input(f"Inserisci il numero (tra 1 e 30): "))
        if 1 <= num <= 30:
            numeri.append(num)
            break
        else:
            print("Il numero deve essere compreso tra 1 e 30. Riprova.")

# eseguo il print dell'output
for num in numeri:
    print('*' * num)
