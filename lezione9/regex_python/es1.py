'''
Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti.

Esempio:

is_integer("123")      # True
is_integer("-456")     # True
is_integer("12.3")     # False'''

def is_integer(s:float) ->bool:
    if s % 1 == 0:
        return True
    else:
        return False
    
print(is_integer(4))
print(is_integer(4.5))