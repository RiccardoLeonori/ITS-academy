import string

def count_unique_words(text):
    parole = {}
    
    tokens = text.split()
    
    for token in tokens:
        parola = token.lower()
        parola = parola.strip(string.punctuation)
        
        if parola != "":
            if parola in parole:
                parole[parola] += 1 
            else:
                parole[parola] = 1
    
    return parole


text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
print(output)

text2 = "Ciao! Come stai? Tutto bene, grazie. E tu, come stai?"
print(count_unique_words(text2))
