n = int(input("Inserisci un numero intero positivo: "))
cont = 0
i = 0
if n % 1 == 0 and n > 0:
    for i in range(11):
        x = int(input("Inserisci un numero: "))
        if x % n == 0:
            cont += 1
    print(f"{cont} numeri sono divisibili per il numero iniziale")
else:
    print("Inserisci un numero intero positivo")