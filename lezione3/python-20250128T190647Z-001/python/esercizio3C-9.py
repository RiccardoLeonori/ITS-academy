'''Esercizio 3C-9. 
Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) 
e salvi le coordinate inserite in una tupla. Utilizzare il  match statement per determinare la sua posizione 
del punto inserito nel piano cartesiano:

- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."'''

'''
primo metodo (non avevo letto di dover usare le tuple)

x = int(input("Inserisci la coordinata x: "))
y = int(input("Inserisci la coordinata y: "))

punto = (x, y)

match punto:
    case (0, 0):
        print("Il punto si trova nell'origine.")
    case (_, 0):
        print("Il punto si trova sull'asse X.")
    case (0, _):
        print("Il punto si trova sull'asse Y.")
    case (x, y) if x > 0 and y > 0:
        print("Il punto si trova nel primo quadrante.")
    case (x, y) if x < 0 and y > 0:
        print("Il punto si trova nel secondo quadrante.")
    case (x, y) if x < 0 and y < 0:
        print("Il punto si trova nel terzo quadrante.")
    case (x, y) if x > 0 and y < 0:
        print("Il punto si trova nel quarto quadrante.")'''




def punto(*punti):

    match punti:
        case (0, 0):
            print("Il punto si trova nell'origine.")
        case (_, 0):
            print("Il punto si trova sull'asse X.")
        case (0, _):
            print("Il punto si trova sull'asse Y.")
        case (x, y) if x > 0 and y > 0:
            print("Il punto si trova nel primo quadrante.")
        case (x, y) if x < 0 and y > 0:
            print("Il punto si trova nel secondo quadrante.")
        case (x, y) if x < 0 and y < 0:
            print("Il punto si trova nel terzo quadrante.")
        case (x, y) if x > 0 and y < 0:
            print("Il punto si trova nel quarto quadrante.")

x = int(input("Inserisci la coordinata x: "))
y = int(input("Inserisci la coordinata y: "))

punto(x, y)