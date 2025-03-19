'''Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, 
terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''

# loop infinito finchè l'utente non digita "fine"
while True:
    parola = str(input("Inserisci una parola (digita \"fine\" per terminare): "))
    
    # controlla se la parola inserita è "fine"
    if parola == "fine":
        break

    # controlla se il primo carattere e l'ultimo sono uguali
    if parola[0] == parola[-1]:
        print(f"La parola \"{parola}\" ha il primo e l'ultimo carattere uguali.")
        
    # in caso il primo carattere e l'ultimo non sono uguali
    else:
        print(f"La parola \"{parola}\" non ha il primo e l'ultimo carattere uguali.")