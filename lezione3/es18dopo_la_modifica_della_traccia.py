i = 1
media = 0
sum_pari = 0
sum_disp = 0
n = int(input("Quante iterazioni vuoi fare? > "))
while(True):
    for i in range(1, n+1):
        num = int(input("Inserisci il numero > "))
        media += num
        media = media / i
        if num % 2 == 0 and num > media:
            sum_pari += num
        else:
            sum_disp += num
    break
if sum_pari > sum_disp:
    print(f"La somma dei numeri pari è: {sum_pari} \nLa somma dei numeri dispari è: {sum_disp} \nLa somma dei numeri pari è maggiore della somma dei numeri dispari")
elif sum_pari < sum_disp:
    print(f"La somma dei numeri pari è: {sum_pari} \nLa somma dei numeri dispari è: {sum_disp} \nLa somma dei numeri dispari è maggiore della somma dei numeri dispari")
else:
    print(f"La somma dei numeri pari è: {sum_pari} \nLa somma dei numeri dispari è: {sum_disp} \nLa somma dei numeri pari è uguale alla somma dei numeri dispari")