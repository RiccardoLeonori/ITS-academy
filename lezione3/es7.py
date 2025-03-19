count = 0
sum = 0
media = 0
while(True):
    x = input("Vuoi inserire un voto? (y/n) > ")
    if x == 'y':
        j = input("dammi un numero: ")
        if not j.isnumeric():
            print("Devi inserire un numero intero!")
            continue
        else:
            j = int(j)

        count += 1
        sum += j
    elif x == 'n':
        media = sum/count
        print(f"La media è: {media}")
        break
    else:
        print("Inserisci \"y\" per si oppure \"n\" per no")