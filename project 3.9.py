import turtle
from itertools import cycle

colors=cycle(['red','orange','yellow','blue','purple'])

def draw_shape(size,angle,shift,shape):
    turtle.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        turtle.circle(size)
        next_shape = 'square'
    elif shape =='square':
        for i in range(5):
            turtle.forward(size +10)
            turtle.left(60)
        hext_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size+2, angle+2, shift+2, next_shape)

turtle.bgcolor('black')
turtle.speed('slow')
turtle.pensize(8)
draw_shape(30, 0, 1, 'circle')


