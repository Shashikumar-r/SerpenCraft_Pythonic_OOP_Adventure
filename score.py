from turtle import Turtle
class Score(Turtle):
    #  TODO 5. display  scrore_board

    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_board()

    def score_board(self):
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"score :{self.score}",move=False, align='center',font=("Verdana",15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER",move=False, align='center', font=("Verdana", 15, "normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.score_board()


