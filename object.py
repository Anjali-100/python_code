
# from turtle import Turtle, Screen



# tinny = Turtle()
# print(tinny)
# tinny.shape("turtle")
# tinny = Screen()
# print(tinny.exitonclick())
# print(tinny.canvheight)
# print(tinny.canvwidth)
from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()