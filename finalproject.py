import turtle
import random
import datetime
import time
#timer count
x=0
#def the movement,dirction depends on Axis, forward is distanse
def up():
    jerry.setheading(90)
    jerry.forward(20)
def down():
    jerry.setheading(270)
    jerry.forward(20)
def left():
    jerry.setheading(180)
    jerry.forward(20)
def right():
    jerry.setheading(0)
    jerry.forward(20)
#current date and time
tday=datetime.datetime.now()
#set up a space, create a screen.
playground = turtle.Screen()
#insert pic for tom and jerry(make sure pic and file in the same folder)
playground.register_shape("tom2.gif")
playground.register_shape("jerry2.gif")
#command
playground.onkey(up,'Up')
playground.onkey(down,'Down')
playground.onkey(left,'Left')
playground.onkey(right,'Right')

playground.listen()

#create start screen,title
writer = turtle.Turtle()
writer.color('brown')
writer.hideturtle()
writer.penup()
writer.goto(0,0)
writer.write("Tom & Jerry", align='center',font=('Comic Sans MS',60,'bold'))
writer.goto(300,300)
writer.write((tday),align='right',font=('Comic Sans MS',10,'bold'))
time.sleep(3)
writer.clear()

tom = turtle.Turtle()
tom.shape("tom2.gif")
tom.speed(0)
tom.penup()
#set up tom at random place
tom.goto(random.randint(-200,200),random.randint(-200,200))

jerry = turtle.Turtle()
jerry.shape("jerry2.gif")
#move sppeed
jerry.speed(0)
jerry.penup()
#set up jerry at ramdon place
jerry.goto(random.randint(-200,200),random.randint(-200,200))

#timer display

def countdown(time):
    global x
    x+=1

    playground.ontimer(lambda: countdown(time + 1), 1000)
countdown(0)
#how you face = how to chase
while True:
    tom.setheading(tom.towards(jerry))
    tom.forward(5)
    if tom.distance(jerry) < 10:
        playground.clear()
        #final screen
        jerry.goto(0,0)
        jerry.color('red')
        jerry.write("Game Over!!!", align='center', font=('Comic Sans MS', 60, 'bold'))
        jerry.goto(0,-100)
        jerry.write(f"You survived {x} seconds", align='center', font=('Comic Sans MS', 20, 'bold'))
        jerry.goto(0,-200)
        if x < 5:
            jerry.write("Can you please use your hands?", align='center', font=('Comic Sans MS', 20, 'bold'))

        elif 10 > x >5 :
            jerry.write("You suck!!!",align='center', font=('Comic Sans MS', 20, 'bold'))

        else:
            jerry.write("Good Job",align='center', font=('Comic Sans MS', 20, 'bold'))

        time.sleep(1000)
