'''Esercizio 3
Scrivere un programma che acquisisca una stringa inserita dall'utente e 
generi una nuova stringa che corrisponda alla versione invertita della stringa originale. 
Il programma deve poi visualizzare la stringa ottenuta in output. 
Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

# chiedo all'utente di inserire una parola
stringa = input("Inserisci una stringa: ")

# inizializzazione della stringa invertita come stringa vuota
stringa_invertita = ""

# ciclo per scorrere la stringa dalla fine all'inizio impostando l'indice all'ultimo carattere
i = len(stringa) - 1
while i >= 0:

    # aggiungo il carattere alla stringa invertita
    stringa_invertita += stringa[i]
    i -= 1

# eseguo il print dell'output
print(f"La stringa invertita è: {stringa_invertita}")