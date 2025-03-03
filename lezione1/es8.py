'''
Progetta un algoritmo che dati 7 numeri, trova e comunica i numeri maggiori di un valore soglia fornito dall'utente.'''

soglia = int(input("Scrivi la soglia: "))
cont = 0
while cont < 7:
    n = int(input("Scrivi il numero: "))
    if n > soglia:
        print(f"Numero {n} maggiore della soglia")
    cont += 1
