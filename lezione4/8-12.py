'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that's being ordered. Call the function three times, 
using a different number of arguments each time.'''

def sandwiches(*args):
    print(f"Your sandwiches is compose by:")
    for i in args:
        print(f"{i}")

sandwiches("salad", "tomato", "tuna")
sandwiches("mayo", "tomato", "tuna")
sandwiches("rise", "tomato", "tuna")