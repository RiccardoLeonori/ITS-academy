x = int(input("Inserisci un numero intero: "))
if x % 1 == 0:
    if x % 2 == 0 and x > 10:
        print("Numero valido")
    else:
        print("Numero non valido")
else:
    print("Inserisci un numero intero")