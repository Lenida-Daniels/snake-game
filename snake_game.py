import turtle
import time
import random 

delay= 0.1

#set up the screen
wn= turtle.Screen()
wn.title("Snake Game by @Daniels")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)#turns off the screen updates

#snake head
head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction= "stop"

#snake food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction ="down"

def go_left():
    head.direction ="left"

def go_right():
    head.direction ="right"

def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y= head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x= head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#main game loop
while True:
    wn.update()

    if head.distance(food)<20:
        x= random.randint(-290, 290)
        y= random.randint(-290, 290)
        food.goto(x,y)
        
    move()
    time.sleep(delay)
wn.mainloop()