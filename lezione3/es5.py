n = int(input("dammi un numero positivo intero"))
i = 1
sum = 0
if n > 0 and n % 1 == 0:
    for i in range(n+1):
        sum += i**2
        i += 1
    print(f"la somma è: {sum}")
else:
    print("dammi un numero positivo intero")