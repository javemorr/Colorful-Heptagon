# HOC - Python Workshop #4
# Date: 24 Jan 2021

# Use Random, Turtle
import random
import turtle as t

def get_line_length(): # alternative getLineLength()
    choice = input('Enter line length "long, medium, short":')
    print (choice)
    if choice == 'long':
        line = 250
    elif choice == 'medium':
        line = 200
    else:
        line = 100
    return line

def get_line_width():
    choice = input('Enter line width "superthick, thick, thin":')
    print (choice)    
    if choice == 'superthick':
        line = 40
    elif choice == 'thick':
        line = 25
    else:
        line = 10
    return line

def get_edge_polygon():   
    choice =  input('Enter the number of edges for the polygon "an integer equal to or bigger than 3":')
    print (choice)
    if choice.isdigit() and int(choice) >=3:
        line = int(choice)
    else:
        line = 3
    return line
    
def move_turtle(line_length):
    t.shapesize(2,2,1)
    t.stamp()
    polygon_angle = 360/edge_polygon
    t.right(polygon_angle)
    t.forward(line_length)

# main program
line_length = get_line_length()
line_width = get_line_width()
edge_polygon = get_edge_polygon()
print('The return value is', line_length)
print('The return value is', line_width)
print('The return value is', edge_polygon)

t.shape('turtle')
t.pensize(line_width)
t.bgcolor('black')

# An Infinite Loop for the turtle movement
while True:
    pen_color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
    for i in range(len(pen_color)):
        t.pencolor(pen_color[i])
        t.fillcolor(pen_color[i])
        move_turtle(line_length)
