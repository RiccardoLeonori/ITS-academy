n = int(input("Inserisci un valore: "))
somma = 0
prodotto = 1
if n % 2 == 0:
    for i in range(1, n+1):
        if i % 4 == 0:
            somma += i
    print(f"La somma dei numeri da 1 a {n} che sono divisibili per 4 è: {somma}")
elif n % 2 == 1:
    for i in range(1, n+1):
        if i % 2 == 1:
            prodotto *= i
    print(f"Il prodotto dei numeri dispari da 1 a {n} è: {prodotto}")
else:
    print("Inserisci un numero positivo")