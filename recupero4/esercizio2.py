def printListBackward(lista):
    if not lista:
        return
    printListBackward(lista[1:])
    print(lista[0])


lista1 = [1, 2, 3, 4, 5]
lista2 = ["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]

print("Lista 1 al contrario:")
printListBackward(lista1)

print("\nLista 2 al contrario:")
printListBackward(lista2)
