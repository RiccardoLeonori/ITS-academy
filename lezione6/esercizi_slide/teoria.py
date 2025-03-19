class MyList:
    def __init__(self):
        self.lst = []
    
    def aggiungi(self, val:int):
        self.lst.append(val)

    def find(self , val:int) ->bool:
        return val in self.lst
    
    def __repr__(self):
        return f"{self.lst}"
    

'''mylist = MyList()
mylist2 =  MyList()
mylist.aggiungi(10)
mylist2.aggiungi(10)
print(mylist == mylist2)
print(mylist)
print(mylist2)'''


class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f"Name: {self.name} - Age: {self.age}")
        

p = Person(name = "Luigi", age = 20)
p.print_info()
