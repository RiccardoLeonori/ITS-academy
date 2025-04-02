'''
Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
Handle ValueError if the input is negative by returning an informative message.'''

import math

def safe_sqrt(number:float) -> float:
    
    if number <= 0:
        raise ValueError(f"The number {number} is not positive!!!")
    else:
        x = math.sqrt(number)

    return x


print(safe_sqrt(-1))