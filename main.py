from turtle import Screen
import time
from snake import Snake
from score import Score
from food import Food
# TODO 4 :- creating food
food = Food()
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0)

# TODO 1 :- Create a snake body
snake = Snake()

# TODO 3 :- Control the snake ---> up,down,right,left
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

score = Score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #  TODO 2 :- move and rotaate a snake body
    #           1. 3rd moves to 2nd pos, 2nd moves to 1st pos and 1st moves to forward
    snake.move()


    #  TODO 4.1. detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # TODO 7. add more tails when eat the food
        snake.extend()
        #  TODO 5. display  scrore_board
        score.score_board()
        score.increase_score()

    #TODO 6. detect the collision with wall
    if snake.head.xcor() > 280 or  snake.head.xcor() < -280 or  snake.head.ycor() > 280 or  snake.head.ycor() < -280 :
        game_is_on=False
        score.game_over()


    # TODO 7. detect the collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()