from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments: list[Turtle] = []

    def get_head(self) -> Turtle:
        return self.segments[0]

    def collision_with_tail(self) -> bool:
        head = self.get_head()
        for seg in self.segments[1:]:
            if head.distance(seg) < 10:
                return True

        return False

    def create(self):
        # Starting with snake of length 3
        for _ in range(0, 3):
            self.extend()

    def extend(self):
        new_segment = Turtle(visible=False)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        # give the new segment the same position as the current tail, if it exists
        if len(self.segments) > 0:
            tail_pos = self.segments[-1].position()
            new_segment.goto((tail_pos[0], tail_pos[1]))

        new_segment.showturtle()
        self.segments.append(new_segment)

    def move(self):
        # starting from the tail, move each segment to the position of the one in front
        for i in range(len(self.segments) - 1, 0, -1):
            seg_in_front_pos = self.segments[i - 1].position()
            self.segments[i].goto((seg_in_front_pos[0], seg_in_front_pos[1]))

        # Move the head forward on current heading
        self.segments[0].forward(10)

    def turn_left(self):
        if len(self.segments) > 0:
            new_heading = self.segments[0].heading() + 90
            self.segments[0].setheading(new_heading)

    def turn_right(self):
        if len(self.segments) > 0:
            new_heading = self.segments[0].heading() - 90
            self.segments[0].setheading(new_heading)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create()