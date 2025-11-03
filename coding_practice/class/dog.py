class Dog:
    """This is a simple attempt to model a dog"""

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name.title()} is sitting")
    
    def roll_over(self):
        print(f"{self.name.title()} is now rolling over")


my_dog = Dog('Willie', 6)

my_dog.roll_over()
my_dog.sit()