from turtle import  Turtle,Screen


screen = Screen()
screen.setup(width=600 , height= 500)
color_list=["red","blue","green","yellow","purple","orange"]
positions = [-70 , -40 , -10,20,50,80]
guess = screen.textinput(title="Turtles Racing Game",prompt="Which turtle color will will the race?   ")

for turtle_index in range(0,6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(color_list[turtle_index])
    my_turtle.goto(x=-280, y =positions[turtle_index])




screen.exitonclick()