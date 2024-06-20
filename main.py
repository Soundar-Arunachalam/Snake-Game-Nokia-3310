from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreCard
screen=Screen();
screen.title("NokiaSnaky")
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=ScoreCard()
screen.update()
game_is_on=True
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:


    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with foods
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increaseScore()
        snake.extend()
    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.ycor()<-290 or snake.head.xcor()<-290:
        scoreboard.gameOver()
        game_is_on=False
    #detect collision with  tail
    for segment in snake.segments:
        if segment==snake.head:
            continue
        elif(snake.head.distance(segment)<10):
            game_is_on=False
            scoreboard.gameOver()










screen.exitonclick();