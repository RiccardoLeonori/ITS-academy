'''Esercizio 3C-4. 
Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, 
utilizzando un match statement, identifichi a quale categoria esso appartiene. 
L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,  
mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.'''

nome_animale = str(input("Digita il nome di un animale: "))

match nome_animale:
    case "cane" | "gatto" | "cavallo" | "elefante" | "leone":
        print(f"{nome_animale} appartiene alla categoria dei Mammiferi!")
    case "serpente" | "lucertola" | "tartaruga" | "coccodrillo":
        print(f"{nome_animale} appartiene alla categoria dei Rettili!")
    case "aquila" | "pappagallo" | "gufo" | "falco":
        print(f"{nome_animale} appartiene alla categoria dei Uccelli!")
    case "squalo" | "trota" | "salmone" | "carpa":
        print(f"{nome_animale} appartiene alla categoria dei Pesci!")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {nome_animale}!")

'''altro metodo
mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco"]
pesci = ["squalo", "trota", "salmone", "carpa"]

nome_animale = str(input("Digita il nome di un animale: "))

match nome_animale:
    case nome_animale if nome_animale in mammiferi:
        print(f"{nome_animale} appartiene alla categoria dei Mammiferi!")
    case nome_animale if nome_animale in rettili:
        print(f"{nome_animale} appartiene alla categoria dei Rettili!")
    case nome_animale if nome_animale in uccelli:
        print(f"{nome_animale} appartiene alla categoria dei Uccelli!")
    case nome_animale if nome_animale in pesci:
        print(f"{nome_animale} appartiene alla categoria dei Pesci!")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {nome_animale}!")
'''