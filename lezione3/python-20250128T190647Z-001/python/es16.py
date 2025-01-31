pari = 0
dispari = 0
negativi = 0
pari_maggiori_di_20 = 0
minori_di_meno_10= 0
for i in range(10):
    n = int(input("Inserisci un numero: "))
    if n % 2 == 0 and n > 20 and n > 0:
        pari_maggiori_di_20 += 1
        pari += 1
    elif n <= 0:
        negativi += 1
        if n % 2 == 1:
            dispari += 1
        elif n < -10:
            minori_di_meno_10 += 1
    elif n % 2 == 0:
        pari += 1
print(f"I numeri pari sono: \"{pari}\"")
print(f"I numeri dispari sono: \"{dispari}\"")
print(f"I numeri negativi sono: \"{negativi}\"")
print(f"I numeri pari e maggiori di 20 sono: \"{pari_maggiori_di_20}\"")
print(f"I numeri minori di - 10 sono: \"{minori_di_meno_10}\"")