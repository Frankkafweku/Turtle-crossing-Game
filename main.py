import time
from turtle import Screen
from player import Player
from player import Player2
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
player2 = Player2()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player2.go_up, "w")

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20 or car.distance(player2) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect win
    if player.has_won():
        player.go_to_starting_position()
        car_manager.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()
