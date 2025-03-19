'''Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49.
Write a Python program that compute these three different sums'''

sum = 0
for i in range(1, 11):
    sum += i
print(f"La somma tra 1 e 10 è {sum}")

sum = 0
for i in range(20, 38):
    sum += i
print(f"La somma tra 20 e 37 è {sum}")

sum = 0
for i in range(35, 50):
    sum += i
print(f"La somma tra 35 e 49 è {sum}")