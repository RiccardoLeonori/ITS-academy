'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user's information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.'''

class User:

    def __init__(self, first_name:str, last_name:str, age:int, gender:str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.gender)
    
    def greet_user(self):
        print(f"Hi, {self.first_name} {self.last_name}, welcome!")


mario = User("Mario", "Rossi", 25, "Male")
maria = User("Maria", "Gialli", 25, "Female")
marco = User("Marco", "Verdi", 25, "Male")

mario.describe_user()
mario.greet_user()

maria.describe_user()
maria.greet_user()

marco.describe_user()
marco.greet_user()