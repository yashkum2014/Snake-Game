import turtle
import random
import time
delay=0.1

# 1. setting up the screen
window=turtle.Screen()
window.setup(width=600, height=600)
window.title("snake game edition by Mr.Yk")
window.bgcolor("black")
# stops the animation
window.tracer(0)

# 2.Snake head 
head=turtle.Turtle()
head.speed(0)
head.color("azure")
head.shape("circle")
head.penup()
head.goto(0,0)
head.direction ="stop"

# 2.1 Adding funtionality to move head in all 4 directions
def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20)
    
    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20)

# 2.2 defining functions to give orders to move snake head 
def go_up() :
    head.direction = "up"

def go_down() :
    head.direction = "down"

def go_left() :
    head.direction = "left"

def go_right() :
    head.direction = "right"

# 2.3 command by keyboard to move
window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")

# 3. Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("DarkGreen")
food.penup()
food.goto(0,100)

body = []

# MAIN GAME LOOP
while True:
    #update the screen everytime
    window.update()
    
    # 3.1 move food to random spot
    if head.distance(food) <20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
    
        # 4. Add body
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        new_body.color("cornsilk")
        new_body.penup()
        body.append(new_body)

    # 4.1 move end body segment in reverse order
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x,y)
    
    # 4.2 move body 0 to where the head is 
    if len(body) > 0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)


    move()

    time.sleep(delay)

    window.listen()



# keeps the window open
window.mainloop()
