tutor = 3
lista_attesa = 0
while(True):
    studente = input("vuoi un tutor y/n?")
    if studente == 'y':
        if tutor > 0:
            tutor -= 1
            print("tutor assegnato con successo")
        elif tutor == 0 and lista_attesa <4:
            lista_attesa += 1
            print("sei in lista d'attesa")
        else:
            print("tutti i tutor e la lista di attesa non hanno più posti liberi")
            break
    elif studente == 'n':
        print("arrivederci")
    else:
        print(f"inserisci \"y\" per si oppure \"n\" per no")
