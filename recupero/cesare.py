'''
Versione della traccia'''

'''
from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s, key):
    result = []

    for char in s:
        if char in ascii_lowercase:
            index = ascii_lowercase.index(char)
            new_index = (index + key) % 26
            result.append(ascii_lowercase[new_index])
        elif char in ascii_uppercase:
            index = ascii_uppercase.index(char)
            new_index = (index + key) % 26
            result.append(ascii_uppercase[new_index])
        else:
            result.append(char)

    return ''.join(result)

def caesar_cypher_decrypt(s, key):
    return caesar_cypher_encrypt(s, -key)

print(caesar_cypher_encrypt("Hello, World!", 3))
print(caesar_cypher_decrypt("Khoor, Zruog!", 3))

'''


'''
Versione migliore'''

def F1(t, F1:int):
    r = []                                                  # creo una lista vuota
    for c in t:                                             # ciclo sul parametro t con la variabile c
        if c.isalpha():                                     # isalpha() restituisce true se c contiene solo lettere e almeno un carattere altrimenti false
            o = ord('A') if c.isupper() else ord('a')       # prende il codice ascii di a oppure di A a seconda se sia maiuscola o minuscola
            r.append(chr((ord(c) - o + F1) % 26 + o))       
        else:
            r.append(c)
    return ''.join(r)
 
print(F1("synt{U3yy0_Jbeyq}", 39))  # inserire come primo parametro la parola, come secondo il valore numerico per cambiare la posizione


#bruteforce della chiave di cesare (in caso non si conosce)
'''
for i in range(27):
    print(F1("synt{U3yy0_Jbeyq}", i))
'''