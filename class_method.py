# class MyClass:
#     class_variable = "I am a class variable"

#     def __init__(self, value):
#         self.instance_variable = value

#     def instance_method(self):
#         return f"Instance method: {self.instance_variable}"

#     @classmethod
#     def class_method(cls):
#         return f"Class method: {cls.class_variable}"

# # Creating an instance
# obj = MyClass("I am an instance variable")

# # Accessing instance method
# result1 = obj.instance_method()

# # Accessing class method
# result2 = MyClass.class_method()

# print(result1)
# print(result2)


class Car:
    # Class variable to count all cars
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # When a new car is made, we update the total number of cars
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

# Creating some cars
car1 = Car("Toyota", "Camry")
total = Car.get_total_cars()
print(f"Total cars made: {total}")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

# Now, let's use the class method
total = Car.get_total_cars()
print(f"Total cars made: {total}")
