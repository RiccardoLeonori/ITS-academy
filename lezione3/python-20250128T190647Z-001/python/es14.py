d1 = int(input("Lancia un d6 e inserisci il risultato: "))
d2 = int(input("Lancia un d6 e inserisci il risultato: "))
sum = 0
punteggio = 0
if d1 >= 0 and d1 <= 6 and d2 >= 0 and d2 <= 6:
    sum = d1 + d2
    print(f"Il risultato di entrambi i dadi è {sum}")
    while(True):
        d1 = int(input("Lancia un d6 e inserisci il risultato: "))
        d2 = int(input("Lancia un d6 e inserisci il risultato: "))
        if d1 % 2 == 0 and d2 % 2 == 0 and sum > 8:
            punteggio += 100
            print("Hai vinto")
            break
        elif d1 == 6 or d2 == 6 or sum == 7:
            punteggio += 10
        else:
            print("Hai perso")
            break
else:
    print("Sei sicuro di aver lanciato un d6 (dado a 6 faccie)")