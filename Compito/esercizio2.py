'''Esercizio 2
Scrivere un programma che acquisisca una stringa inserita dall'utente e 
calcoli il numero totale di spazi presenti nella stringa. 
Il risultato deve essere visualizzato in output.'''

# chiedo all'utente di inserire una parola
stringa = input("Inserisci una stringa: ")

# inizializzo la variabile numero_spazi a 0 per contare gli spazi
numero_spazi = 0

# ciclo for che scorre tutta la stringa
for carattere in stringa:

    # controllo se ci sono spazi e in caso aumento la variabile numero_spazi
    if carattere == " ":
        numero_spazi += 1

# eseguo il print dell'output
print(f"Il numero totale di spazi nella stringa è: {numero_spazi}")