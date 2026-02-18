# Instance methods and self

class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is driving")

car1 = Car("Toyota")
car1.drive()
