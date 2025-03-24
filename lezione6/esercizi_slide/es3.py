'''
Given is the class Animal. For each task, test your changes!
1. Create two realistic instances of Animals
2. Print the name of each object
3. Change the amount of legs of one object using the dot notation
4. Add a method setLegs() to set the legs of an object and repeat task 3 but
this time using the method.
5. Add a method getLegs() to return the amount of legs
6. Add a method named printInfo that prints all attributes of the Animal'''

class Animal:
    def __init__(self,  name:str, legs:int):
        self.name = name
        self.legs = legs

    def setLegs(self, new_legs:int):
        self.legs = new_legs

    def getLegs(self):
        return self.legs
    
    def printInfo(self):
        print(self.name)
        print(self.legs)


ippopotamo = Animal("Gennaro", 4)
aquila = Animal("Nino", 2)

print(ippopotamo.name)
print(aquila.name)


aquila.legs = 1
print(aquila.legs)


aquila.setLegs(3)
print(aquila.legs)


print(aquila.getLegs())


aquila.printInfo()