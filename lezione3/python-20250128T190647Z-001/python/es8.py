a = int(input("Dammi un numero positivo: "))
b = int(input("Dammi un numero positivo più grande: "))
sum = 0
i = a
if a > 0 and b > 0 and a % 1 == 0 and b & 1 == 0 and a < b:
    for i in range(a, b+1):
        sum += i
    print(f"{sum}")
else:
    print("Inserire due valori interi positivi dove il primo è minore del secondo")