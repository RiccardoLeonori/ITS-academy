x = int(input("dammi un numero positivo"))
lista_numeri:list = []
sum = 0
if x > 0:
    for i in range(10):
        lista_numeri.append(int(input("dammi un numero")))
        print(f"{lista_numeri}")
    if x % 2 == 0:
        metà_x = x / 2
        for numero in lista_numeri:
            if numero > metà_x:
                sum += numero
    else:
        for numero in lista_numeri:
            if numero < x:
                sum += numero
    print(f"La somma dei numeri selezionati è: {sum}")
else:
    print("inserisci un numero positivo")