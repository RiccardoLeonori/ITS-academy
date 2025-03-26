'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant() for each instance.'''


class Restaurant:
    def __init__(self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is open!!!")

restaurant = Restaurant("Sushi&Co", "Japanese")
restaurant2 = Restaurant("Meet&Co", "Africans")
restaurant3 = Restaurant("Fish&Co", "English")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()