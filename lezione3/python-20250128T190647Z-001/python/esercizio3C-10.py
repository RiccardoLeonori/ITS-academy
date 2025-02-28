'''
Esercizio 3C-10. 
Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), 
salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → "2 Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data." '''

def data(*args):

    match args:
        case (1, 1):
            print(f"Il {giorno}/{mese} èCapodanno")
        case (14, 2):
            print(f"Il {giorno}/{mese} è San Valentino")
        case (2, 6):
            print(f"Il {giorno}/{mese} è Festa della Repubblica Italiana")
        case (15, 8):
            print(f"Il {giorno}/{mese} è Ferragosto")
        case (31, 10):
            print(f"Il {giorno}/{mese} è Halloween")
        case (25, 12):
            print(f"Il {giorno}/{mese} è Natale")
        case _:
            print("Nessuna festività importante in questa data.")

giorno = int(input("Scrivi il giorno: "))
mese = int(input("Scrivi il mese: "))

data(giorno, mese)