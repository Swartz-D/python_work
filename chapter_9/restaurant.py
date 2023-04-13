"""simple restaurant"""


class Restaurant:
    """simple example of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """prints the name and type of food"""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """prints the name and open"""
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, customers):
        """sets number served to customers"""
        self.number_served = customers
        print(self.number_served)

    def increment_number_served(self, new_customers):
        """increments number served"""
        self.number_served += new_customers
        print(self.number_served)


restaurant = Restaurant("Irishai", "Japanese")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(20)
restaurant.increment_number_served(7)
