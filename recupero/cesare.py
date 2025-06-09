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