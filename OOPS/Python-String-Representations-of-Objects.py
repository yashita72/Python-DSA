class Car:
    def __init__(self, maximum_speed, unit):
        self.maximum_speed = maximum_speed
        self.unit = unit

    def __str__(self):
        return f"Car with the maximum speed of {self.maximum_speed} {self.unit}"


class Boat:
    def __init__(self, maximum_speed):
        self.maximum_speed = maximum_speed

    def __str__(self):
        
        return f"Boat with the maximum speed of {self.maximum_speed} knots"
