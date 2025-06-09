def ricerca_binaria(lista, numero):
    inizio = 0
    fine = len(lista) - 1
    
    while inizio <= fine:
        centro = (inizio + fine) // 2
        
        if lista[centro] == numero:
            return True
        elif numero < lista[centro]:
            fine = centro - 1
        else:
            inizio = centro + 1
    
    return False


numeri = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(ricerca_binaria(numeri, 7))
print(ricerca_binaria(numeri, 6))
print(ricerca_binaria(numeri, 1))
print(ricerca_binaria(numeri, 20))