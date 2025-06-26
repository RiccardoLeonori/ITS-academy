def calculateCharges(ora: int) -> int:
    
    pagamento = 0
    if ora % 1 == 0:
        pass
    else:
        ora += 1
        ora //= 1

    if ora > 3 and ora < 19:
        pagamento = ((ora - 3) * 0.50) + 2
        return pagamento
    elif ora > 0 and ora <= 3:
        pagamento = 2
        return pagamento
    elif ora >= 19:
        pagamento = 10
        return pagamento
    else:
        return f"Errore, hai inserito un numero sbagliato"


'''
ora = float(input("Inserisci il numero: "))
print(calculateCharges(ora))
'''

tests = [1.5, 4.0, 5.5, 24]
result = []
print(f"{'Car' :<5}", end = "   ")
print(f"{'Hours' :<5}", end = "   ")
print(f"{'Charge' :<5}")

for i in range(len(tests)):
    result.append(calculateCharges(tests[i]))
    print(f"{i+1:<5}", end ="   ")
    print(f"{tests[i]:<5}", end ="   ")
    print(f"{str(calculateCharges(tests[i])) + '$':<5}")

print(f"{'TOTAL':<5}", end = "   ")
print(f"{sum(tests):<5}", end = "   ")
print(f"{str(sum(result)) + '$':<5}")