from turtle import Turtle,Screen
starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake(Turtle):
    # TODO 1 :- Create a snake body
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # TODO 7. add more tails when eat the food
    def extend(self):
        self.add_segment(self.segments[-1].position())

    #  TODO 2 :- move and rotaate a snake body
    #           1. 3rd moves to 2nd pos, 2nd moves to 1st pos and 1st moves to forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)


    # TODO 3 :- Control the snake ---> up,down,right,left
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)


