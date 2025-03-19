n = int(input("inserisci i posti disponibili nel garage: "))
if n > 0:
        occupati = 0
        while(True):
            x = input('Enter your option: ')
            if x == "ingresso":
                if occupati < n :
                    occupati += 1
                    print(f"Un veicolo è entrato. Posti occupati: {occupati}/{n}")
                else: 
                    print("Non ci sono posti disponibili")
            elif x == "uscita":
                if occupati > 0:
                    occupati -= 1
                    print(f"Un veicolo è uscito. Posti occupati: {occupati}/{n}")
                else: 
                    print("Non ci sono posti da occupare")
            elif x== "stato":
                print(f"posti occupati:{occupati}, posti liberi:{n-occupati}")
            elif x == "esci":
                break
            else:
                print("Opzione non valida. Scegli tra 'ingresso', 'uscita', 'stato' o 'esci'.")