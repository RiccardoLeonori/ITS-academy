n = int(input("Quante coppie di valori vuoi inserire: "))
i = 0
for i in range(n):
    x = int(input("Inserisci il primo numero: "))
    y = int(input("Inserisci il secondo numero: "))
    if x > 0 and y > 0:
        prod = x * y
        print(f"Il prodotto è {prod}")
    elif x < 0 and y < 0:
        print("Errore hai inserito 2 numeri negativi")
    else:
        sum = x + y
        print(f"La somma è {sum}")