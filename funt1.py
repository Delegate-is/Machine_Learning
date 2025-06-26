import turtle
import math
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Infinite Hearts")
screen.tracer(0)  # Disable auto-update for smoother animation

t = turtle.Turtle()
t.speed(0)
t.hideturtle()  # Hide the turtle cursor

def heart(n, scale=1):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x * scale, y * scale

def draw_random_heart():
    # Random position, color, and scale
    x_pos = random.randint(-300, 300)
    y_pos = random.randint(-200, 200)
    scale = random.uniform(0.5, 2.5)
    color = (random.random(), random.random(), random.random())  # RGB
    
    t.penup()
    t.goto(x_pos, y_pos)
    t.pendown()
    t.color(color)
    t.begin_fill()
    
    # Draw heart
    for i in range(0, 628, 5):  # 0 to 2π (628 = 100*2π)
        angle = i / 100
        x, y = heart(angle, scale)
        t.goto(x_pos + x, y_pos + y)
    
    t.end_fill()

# Main loop: Keep drawing hearts until screen is filled
counter = 0
max_hearts = 50  # Clear screen after this many hearts

while True:
    draw_random_heart()
    screen.update()  # Manually refresh screen
    time.sleep(0.1)  # Adjust speed
    
    counter += 1
    if counter >= max_hearts:
        t.clear()  # Reset screen
        counter = 0