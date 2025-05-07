# Defining the class

class Car:
    def __init__(self, brand, color):
        self.brand = brand    # attribute
        self.color = color    # attribute
        self.speed = 0        # attribute with default value

    def accelerate(self, honk):
        self.speed += 10
        print(honk)
        print(f"The {self.color} {self.brand} accelerates to {self.speed} km/h")

    def brake(self):
        self.speed = max(0, self.speed - 10)
        print(f"The {self.color} {self.brand} slows down to {self.speed} km/h")


import ipdb; ipdb.set_trace()

# Create objects (instances of the Car class)
car1 = Car("Toyota", "red")
car2 = Car("BMW", "blue")

# Use methods on the objects
car1.accelerate(100)  # The red Toyota accelerates to 10 km/h
print(car1.speed)
#car1.accelerate()  # The red Toyota accelerates to 20 km/h
#car1.brake()       # The red Toyota slows down to 10 km/h

#car2.accelerate()  # The blue BMW accelerates to 10 km/h

