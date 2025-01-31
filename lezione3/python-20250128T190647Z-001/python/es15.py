n = int(input("Inserisci un numero intero: "))
sum = 0
if n % 1 == 0:
    if n >0 and n < 101:
        for i in range(n+1):
            if i % 2 == 0:
                sum += i
        print(f"La somma è {sum}")
    elif n <= 0:
        print("Errore, inserisci un numero positivo")
    else:
        for i in range(n+1):
            if i % 2 == 1:
                sum += i
        print(f"La somma è {sum}")
else:
    print("Inserisci un numero intero")