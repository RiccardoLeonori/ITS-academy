n = 100
occupati = 0
while(True):
    x = input('Enter your option: ')
    if x == "iscrivi":
        if occupati < n :
            occupati += 1
            print(f"Un veicolo è entrato. Posti occupati: {occupati}/{n}")
        else: 
            print("Non ci sono posti disponibili")
    elif x == "annulla":
        if occupati > 0:
            occupati -= 1
            print(f"Un veicolo è uscito. Posti occupati: {occupati}/{n}")
        else: 
            print("Non ci sono posti da occupare")
    elif x== "visualizza":
        print(f"posti occupati:{occupati}, posti liberi:{n-occupati}")
    elif x == "elimina":
        nuovo_corso = input("Nome nuovo corso:")
        n = 100
        occupati = 0
    elif x == "esci":
        break
    else:
        print("Opzione non valida. Scegli tra 'iscrivi', 'annulla', 'visualizza' o 'esci'.")