import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=250, starty= 350)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
# screen.onkey(player.left, "Left")
# screen.onkey(player.right, "Right")

game_is_on = True



while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            print("Turtle hit a car")
            game_is_on = False
            scoreboard.game_over()

    # detect if player reaches other side and updates scoreboard
    if player.ycor() > 280:
        print("Turtle has reached the other side")
        scoreboard.update_score()
        player.reset_position()
        car_manager.increase_speed()


screen.exitonclick()