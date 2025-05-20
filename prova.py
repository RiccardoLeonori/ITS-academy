x = int(input("Inserisci un numero: "))
if x < 0:
    print("Inserisci un numero positivo")
else:
    if x % 2 == 0:
        x /= 2
    else:
        x = x*3+1
    print(x)