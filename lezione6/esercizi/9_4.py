'''
9-4. Number Served: Start with your program from Exercise 9-1. 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again. 
Add a method called increment_number_served() that lets you increment the number of customers who've been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business. '''


class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is open!!!")

    def show_number_served(self):
        print(f"The restaurant have been served {self.number_served} customers")
    
    def set_number_served(self, n:int):
        self.number_served = n

    def increment_number_served(self, increase_customer:int):
        self.number_served += increase_customer


restaurant = Restaurant("Sushi&Co", "Japanese")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.show_number_served()

restaurant.number_served = 30
restaurant.show_number_served()

restaurant.set_number_served(75)
restaurant.show_number_served()

restaurant.increment_number_served(20)
restaurant.show_number_served()