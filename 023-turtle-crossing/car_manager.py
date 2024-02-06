from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars: list[Turtle] = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_another_car(self):
        self.cars.append(self.create_car())

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)
            if self.remove_car(car):
                self.cars.remove(car)

        # Another way of cleaning up the list of cars using inplace slice
        # self.cars[:] = [car for car in self.cars if not self.remove_car(car)]

    @staticmethod
    def remove_car(car: Turtle):
        # Remove cars that have reached the left-hand edge
        if car.xcor() <= -290:
            car.hideturtle()
            return True
        else:
            return False

    def create_car(self) -> Turtle:
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(300, self.random_y())
        return car

    @staticmethod
    def random_y() -> int:
        while True:
            y = random.randint(-250, 250)
            # Give a pixel of space top and bottom, so no overlapping
            if y % 22 == 0:
                return y

    def has_collided(self, player: Turtle) -> bool:
        for car in self.cars:
            if car.distance(player) < 20:
                return True

        return False

    def level_up(self):
        self.speed += MOVE_INCREMENT
