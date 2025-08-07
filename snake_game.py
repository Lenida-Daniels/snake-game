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
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments =[]

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

    #check for a collision with the food
    if head.distance(food)<20:
        x= random.randint(-290, 290)
        y= random.randint(-290, 290)
        food.goto(x,y)

        #add a segment
        new_segment =turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    #move the end segments first in reverse order
    for index in range (len(segments)-1,0,-1):
            x=segments[index-1].xcor() #get the x-coordinate of the segment in front
            y=segments[index-1].ycor() #get the y-coordinate of the segment in front
            segments[index].goto(x,y)  #move the current segment to that position

    #move segment 0 to where the head is
    if len(segments) > 0:
            x=head.xcor()
            y=head.ycor()
            segments[0].goto(x,y)





        


    move()
    time.sleep(delay)
wn.mainloop()