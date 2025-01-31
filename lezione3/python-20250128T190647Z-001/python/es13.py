x = int(input("Dammi un numero: "))
y = int(input("Dammi un numero: "))
z = int(input("Dammi un numero: "))
if x % 1 == 0 and y % 1 == 0 and z % 1 == 0:
    if (x + y + z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
        print("Regole rispettate")
    else:
        print("Regole non rispettate")
else:
    print("Errore: inserisci numeri interi")