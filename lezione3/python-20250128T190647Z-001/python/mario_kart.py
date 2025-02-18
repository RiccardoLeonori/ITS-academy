n = int(input("Dammi un numero e ti dirò la posizione in cui ti trovi: "))
if n % 1 == 0 and n > 0:
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")
else:
    print("Hai messo un numero non valido")