'''
Teofilo A Serpa
P4LAB1
11/7/24
Write a turtle graphics programs that draws a triangle and a square using loops.
'''
import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor("grey")

t.pensize(15)
t.pencolor("teal")
t.shape("arrow")

#while loop to draw square
numb = 0

while numb < 4:
    print("draw a side!")
    numb += 1
    t.forward(100)
    t.right(90)
print("this is where it ends...")

#For loop to draw a triangle
for tr in range (0,3):
    print("Draw that side!")
    t.left(120)
    t.forward(120)
print("Oh yeah! thats how its done!")
