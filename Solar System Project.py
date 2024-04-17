from turtle import *

'''
Background is black

Orange planet is 60px in radius
Grey planet is 20px in radius
Red planet is 40px in radius
Green planet is 30px in radius

Distance from orange planet to grey planet is 100px
Distance from grey planet to red planet is 80px
Distance from red planet to green planet is 90px

'''
# If zero (0) it is drawn instant otherwise it can range between one (1) and ten (10) with one (1) being the slowest speed and ten (10) being the fastest speed
speed(0)
# setting the background colour to BLACK
bgcolor("black")

# create the ORANGE planet
color("orange")
begin_fill()
circle(60)
end_fill()

# move FORWARD
penup()
forward(100)
pendown()

# create the GREY planet
color("gray")
begin_fill()
circle(20)
end_fill()

# move FORWARD
penup()
forward(80)
pendown()

# create the RED planet
color("red")
begin_fill()
circle(40)
end_fill()

# move FORWARD
penup()
forward(90)
pendown()

# create the GREEN planet
color("green")
begin_fill()
circle(30)
end_fill()

# freezes the screen so you have to manually close it
done()