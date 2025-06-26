import turtle
import math
import time

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")
t.pensize(2)

def heart(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

# Draw the heart in a smooth loop
def draw_heart():
    for i in range(0, 628, 5):  # 0 to 2π (628 = 100*2π)
        angle = i / 100  # Convert to radians
        x, y = heart(angle)
        t.goto(x * 10, y * 10)  # Scale up
        t.pendown()
    
    for i in range(628, 0, -5):  # Rewind
        angle = i / 100
        x, y = heart(angle)
        t.goto(x * 10, y * 10)
    
    t.clear()  # Reset for loop

# Infinite animation loop
while True:
    t.penup()
    t.goto(0, 0)
    draw_heart()
    time.sleep(0.1)  # Pause briefly
    