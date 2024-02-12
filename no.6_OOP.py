# Create a simple class with attributes and methods.
# Instantiate objects from the class and their methods.

class cars:
    def __init__(self, car_brand, car_color, car_model):
        self.car_brand = car_brand
        self.car_color = car_color
        self.car_model = car_model


car_Owner1 = cars("Ford", "Red", "Raptor")
car_Owner2 = cars("Toyota", "Blue", "Camry")
car_Owner3 = cars("Honda", "Black", "Civic")

print(car_Owner1.car_brand)
print(car_Owner2.car_color)
print(car_Owner3.car_model)