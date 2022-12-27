import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Game")
screen.tracer(0)

screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.player_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.car_move()
    screen.update()

    # Check whether turtle crossed the road
    if player.ycor() > 250:
        scoreboard.update_scoreboard()


screen.exitonclick()
