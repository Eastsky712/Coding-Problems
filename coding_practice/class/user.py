class User:
    def __init__(self, first_name, last_name, age, height, weight):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first} {self.last}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
    
    def greet_user(self):
        print(f"Hello {self.first} {self.last}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0



