'''
Progetta un algoritmo per trovare il massimo fra quattro numeri inseriti dall'utente.'''

# ciclo while
max = int(input("Scrivi il numero: "))
i = 1
while i < 4:
    i += 1
    n = int(input("Scrivi il numero: "))
    if n > max:
        max = n
print(f"Il numero massimo è {max}")

#ciclo repeat
max = int(input("Scrivi il numero: "))
i = 1
while True:
    i += 1
    n = int(input("Scrivi il numero: "))
    if n > max:
        max = n
    if i ==4:
        break
print(f"Il numero massimo è {max}")

#ciclo for
max = int(input("Scrivi il numero: "))
i = 0
for i in range(3):
    i += 1
    n = int(input("Scrivi il numero: "))
    if n > max:
        max = n
print(f"Il numero massimo è {max}")