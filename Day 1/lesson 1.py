from turtle import *

#we want to paint a house
speed(10)
shape("arrow")
width (4)
color ("Black")
forward(200)
left (90)

forward(200)
left (90) 

forward(200)
left (90)

forward(200)
left (90)

#end of square

#drawin a door 

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#drawin a cellar

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawin windows 


penup()
goto(20,175 )
pendown()
color("blue")
begin_fill()
left(120)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()

penup()
goto(140, 175)
pendown()

begin_fill()
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()

penup()
goto(-455,-15)
pendown()
right(90)
begin_fill()
color("green")
forward(900)
right(90)
forward(300)
right(90)
forward(900)
right(90)
forward(300)
end_fill()




exitonclick()
