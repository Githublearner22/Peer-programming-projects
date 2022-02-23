from turtle import Turtle, Screen
import random

# variables
speed = 1
blobCoords = []
snake_pos = []

canvas = Screen()
canvas.setup(width=200, height=200, startx=0, starty=0)
canvas.bgcolor('white')

snake = Turtle()
snake.shape("square")
snake.color('red')
snake.penup()

def addBlob():
  # this function adds a blob
  blob = Turtle()
  blob.pensize(0.1)
  blob.penup()
  blob.shape("circle")
  blob.color('blue')
  x = random.randint(-150, 150)
  y = random.randint(-150, 150)
  blob.sety(y)
  blob.setx(x)
  blobCoords.append((x,y,blob))

def increaseSize():
    size = snake.turtlesize()
    stepSize = 0.1
    
    snake.turtlesize(stretch_wid=None, stretch_len=size[1]+stepSize, outline=None)

def travel():
    snake.forward(speed)
    canvas.ontimer(travel, 10)
    snakeX = snake.position()[0]
    snakeY = snake.position()[1]
    snake_pos.append(snakeX)
    snake_pos.append(snakeY)
    
    # loop through the array and check that the snake isn't
    for blobPosition in blobCoords:
      blobX = int(blobPosition[0])
      blobY = int(blobPosition[1])
      blobInstance = blobPosition[2]
      distanceFromBlobX = abs(snakeX - blobX)
      distanceFromBlobY = abs(snakeY - blobY)

    if distanceFromBlobX < 10 and distanceFromBlobY < 10:
      blobInstance.hideturtle()
      increaseSize()
      addBlob()

    
canvas.onkey(lambda: snake.setheading(90), 'Up')
canvas.onkey(lambda: snake.setheading(180), 'Left')
canvas.onkey(lambda: snake.setheading(0), 'Right')
canvas.onkey(lambda: snake.setheading(270), 'Down')

canvas.onkey(lambda: addBlob(), 'e')

canvas.onkey(lambda: increaseSize(), 'g')

canvas.listen()

addBlob()
travel()

canvas.mainloop()

print(list(blobCoords))
print(snake_pos)