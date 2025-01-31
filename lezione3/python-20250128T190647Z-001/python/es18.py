x = int(input("Quanti numeri vuoi inserire: "))
pari_maggiori_della_media = 0
dispari_o_minori_della_media = 0
lista:list = []
media = 0
for i in range(x):
    j = int(input("Dammi il numero scelto: "))
    media += j
    lista.append(j)
media = media / x
for i in range(x):
    if lista[i] % 2 == 0 and lista[i] > media:
        pari_maggiori_della_media += lista[i]
    elif lista[i] % 2 == 1 or lista[i] < media:
        dispari_o_minori_della_media += lista[i]
print(f"La somma dei numeri pari e maggiori nella media è: {pari_maggiori_della_media}")
print(f"La somma dei numeri dispari o minori nella media è: {dispari_o_minori_della_media}")