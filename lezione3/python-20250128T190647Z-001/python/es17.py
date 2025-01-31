temperatura_max = float('-inf')
temperatura_min = float('inf')
x = 0
media = 0
while(True):
    for i in range(1, 8):
        x = int(input("Inserisci la temperatura del giorno: "))
        media += x
        if x >= 10 and x <=30:
            print("Temperatura nella norma")
        elif x >= 35:
            print("Allerta temperatura troppo alta")
            if x > temperatura_max:
                temperatura_max = i
        elif x <= 5:
            print("Allerta temperatura troppo bassa")
            if x < temperatura_min:
                temperatura_min = i
        else:
            print("Allerta temperatura")
    break
media = media / 7
print(f"La temperatura media è: {media}")
print(f"La temperatura massima è stata raggiunta il giorno: {temperatura_max}")
print(f"La temperatura minima è stata raggiunta il giorno: {temperatura_min}")