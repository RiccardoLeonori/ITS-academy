'''
1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.'''

'''class student:

    def __init__(self, name:str, studyProgram:str):
        self.name = name
        self.study = studyProgram

    def printInfo(self):
        print(f"{self.name} study {self.study}")
    
federico = student("Federico", "Paint")
riccardo = student("Riccardo", "Python")
jacopo = student("Jacopo", "Minion")

federico.printInfo()
riccardo.printInfo()
jacopo.printInfo()
'''

class student:

    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.study = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"{self.name} study {self.study}, is age is {self.age} and identified as {self.gender}")
    
federico = student("Federico", "Paint", 29, "M")
riccardo = student("Riccardo", "Python", 26, "M")
jacopo = student("Jacopo", "Minion", 19, "M")

federico.printInfo()
riccardo.printInfo()
jacopo.printInfo()