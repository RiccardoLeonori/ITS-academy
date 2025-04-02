import random



def tartaruga(posizione):

    i = random.randint(1, 10)
    
    if 1 <= i <= 5:
        posizione += 3
    elif 6 <= i <= 7:
        posizione -= 6
        if posizione < 1:
            posizione = 1
    else:
        posizione += 1
    
    if posizione > 70:
        posizione = 70
    
    return posizione

def lepre(posizione):

    i = random.randint(1, 10)
    
    if 1 <= i <= 2:
        pass
    elif 3 <= i <= 4:
        posizione += 9
    elif i == 5:
        posizione -= 12
        if posizione < 1:
            posizione = 1
    elif 6 <= i <= 8:
        posizione += 1
    else:
        posizione -= 2
        if posizione < 1:
            posizione = 1
    
    if posizione > 70:
        posizione = 70
    
    return posizione


def gara():
    posizione_tartaruga = 1
    posizione_lepre = 1

    tabellone = ("_ " * 70)

    print("BANG !!!!! AND THEY'RE OFF !!!!!")


print(tartaruga(4))