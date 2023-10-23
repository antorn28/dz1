# друге завдання

class Car:
    fuel_type = "Unknown"
    wheel_count = 4

    def __init__(self, make, model, year, color, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"The {self.color} {self.year} {self.make} {self.model} is accelerating. Current speed: {self.speed} km/h")

    def brake(self, decrement):
        if self.speed - decrement < 0:
            self.speed = 0
        else:
            self.speed -= decrement
        print(f"The {self.color} {self.year} {self.make} {self.model} is braking. Current speed: {self.speed} km/h")

    def honk(self):
        print(f"The {self.color} {self.year} {self.make} {self.model} is honking. Honk! Honk!")

car1 = Car(make="Toyota", model="Camry", year=2022, color="Blue")
car2 = Car(make="Ford", model="Mustang", year=2023, color="Red")

car1.accelerate(20)
car1.brake(5)
car1.honk()

car2.accelerate(15)
car2.honk()