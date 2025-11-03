class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} and it serves {self.type}")
    
    def open_restaurant(self):
        print(f"{self.name.title()} is Open!")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry','banana','peach','mango']

    def get_flavors(self):
        return self.flavors



