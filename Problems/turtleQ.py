import turtle 

'''
Square
p = turtle.Turtle()
for _ in range(4):
    p.forward(100)
    p.left(90)
'''

'''
Triangle
p = turtle.Turtle()
for _ in range(3):
    p.forward(100)
    p.right(120)
'''

'''
Star
p = turtle.Turtle()
for _ in range(5):
    p.forward(100)
    p.right(144)
'''

'''
Shapes
s = turtle.Turtle()
s.shape("square")
'''

'''
Parallelogram
p = turtle.Turtle()
for i in range(2):
    p.forward(100)
    p.left(60)
    p.forward(100)
    p.left(120)
'''

'''
Some spiral
p = turtle.Turtle()
for x in range(360):

    p.width(x / 100 + 1)

    p.forward(x)

    p.left(59)
    
'''


# initialising variables
dist = 1
flag = 500
 
# initialising turtle
spiral = turtle.Turtle()
 
# changing speed of turtle
spiral.speed(10)
 
# making pattern
while flag:
   
    # makes the turtle to move forward
    spiral.forward(dist)
     
    # makes the turtle to move left
    spiral.left(120)
    spiral.left(1)
    dist += 1
    flag -= 1
 
turtle.done()
turtle.done()