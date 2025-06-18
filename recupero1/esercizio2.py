def leggi_intero_positivo(messaggio):
    while True:
        try:
            valore = input(messaggio)
            numero = float(valore)
            
            if numero.is_integer() and numero > 0:
                return int(numero)
            else:
                print("Errore: inserire un numero intero positivo.")
        except ValueError:
            print("Errore: inserire un numero intero positivo.")

def leggi_sequenza():
    sequenza = []
    
    while True:
        try:
            valore = input("Inserisci un numero intero positivo (0 per terminare): ")
            numero = float(valore)
            
            if numero.is_integer() and numero >= 0:
                numero_intero = int(numero)
                
                if numero_intero == 0:
                    break
                else:
                    sequenza.append(numero_intero)
            else:
                print("Errore: inserire un numero intero positivo.")
        except ValueError:
            print("Errore: inserire un numero intero positivo.")
    
    return sequenza

def conta_occorrenze(sequenza, x):
    contatore = 0
    
    for numero in sequenza:
        if numero == x:
            contatore = contatore + 1
    
    return contatore

def trova_prima_posizione(sequenza, x):
    for i in range(len(sequenza)):
        if sequenza[i] == x:
            return i + 1
    
    return -1

def somma_valori_diversi(sequenza, x):
    somma = 0
    
    for numero in sequenza:
        if numero != x:
            somma = somma + numero
    
    return somma