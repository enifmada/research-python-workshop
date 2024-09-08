class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0


    def accelerate(self):
        self.speed += 5
        self.step()

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0
        self.step()

    def step(self):
        assert self.speed >= 0
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time


test_car = Car()
test_car.accelerate()
test_car.brake()
test_car.brake()
print(f"The car has driven {test_car.odometer} miles")
print(f"The car's average speed was {test_car.average_speed()} mph")