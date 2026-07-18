import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

#generating window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

#generating a border for the game
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("black")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#generating snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"


#generating food
food = turtle.Turtle()
food_colors = random.choice(['red', 'green', 'yellow'])
food_shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(food_shapes)
food.color(food_colors)
food.penup()
food.goto(20, 20)

#creating scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 250)
scoreboard.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "bold"))



#assigning key directions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

segments = []

#main game
while True:
    wn.update()

    #checking for collision with border
    if head.xcor() > 280 or head.xcor() < -300 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        wn.clear()
        wn.bgcolor("blue")
        scoreboard.goto(0, 0)
        scoreboard.write("Game Over\n Your Score is: {}".format(score), align="center", font=("Courier", 30, "bold"))
     
    #collision with food
    if head.distance(food) < 20:
        score += 10
        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))


        x_cord = random.randint(-290, 270)
        y_cord = random.randint(-240, 240)
        food_colors = random.choice(['red', 'green', 'yellow'])
        food_shapes = random.choice(['square', 'triangle', 'circle'])
        food.speed(0)
        food.shape(food_shapes)
        food.color(food_colors)
        food.goto(x_cord, y_cord)

        #adding new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)



    #moving the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    #checking for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            wn.clear()
            wn.bgcolor("blue")
            scoreboard.goto(0, 0)
            scoreboard.write("Game Over\n Your Score is: {}".format(score), align="center", font=("Courier", 30, "bold"))

    time.sleep(delay)
turtle.Terminator()