'''
1. Copy the code and print the age of
bob (using the dot notation)
2. Create an if-statement that prints
the name of the oldest of the two
Persons
3. Create three other Persons. Make
a list called people with all 5
Persons.
4. Make a loop that finds and prints
the youngest person's name
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)

if bob.age > alice.age:
    print("bob is the older")
else:
    print("alice is the older")

federico = Person("Federico R.", 29)
jacopo = Person("Jacopo S.", 26)
riccardo = Person("Riccardo L.", 19)

people = [alice, bob, federico, jacopo, riccardo]

min = alice.age
name = alice.name
for i in people:
    if i.age < min:
        min = i.age
        name = i.name

print(f"The youngest person in the group is {i.name}, with {i.age} yo")