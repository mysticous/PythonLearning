import turtle
import time
import random
'''Pixel is the begining of every picture'''


def drawBlock(color, size, position):
    '''need a color (0 or 1) tuple and (width,height) tuple
       position is the top left corner
    '''
    if color == 0:
        c = random.random()
        if c < 0.15:
            color_tuple = (0.6, 0, 0)
        elif c < 0.30:
            color_tuple = (0, 0.6, 0)
        elif c < 0.45:
            color_tuple = (0, 0, 0.6)
        elif c < 0.60:
            color_tuple = (0.6, 0.6, 0)
        elif c < 0.75:
            color_tuple = (0.6, 0, 0.6)
        elif c < 0.9:
            color_tuple = (0, 0.6, 0.6)
        else:
            color_tuple = (0, 0, 0)
    else:
        color_tuple = (1, 1, 1)
    turtle.up()
    turtle.fillcolor(color_tuple)
    turtle.begin_fill()
    turtle.color(color_tuple)
    turtle.pensize(1)
    turtle.goto(position[0], position[1])
    for i in range(4):
        turtle.down()
        turtle.forward(size)
        turtle.right(90)
    turtle.up()
    turtle.end_fill()


def drawBlock_Ex(color, size, position):
    turtle.up()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.color(color)
    turtle.pensize(1)
    turtle.goto(position[0], position[1])
    turtle.down()
    turtle.forward(size[0])
    turtle.right(90)
    turtle.forward(size[1])
    turtle.right(90)
    turtle.forward(size[0])
    turtle.right(90)
    turtle.forward(size[1])
    turtle.right(90)
    turtle.up()
    turtle.end_fill()


def picDraw():
    # blacklist
    Matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0 for i in range(23)],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
        [0 for i in range(23)],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
        [0 for i in range(23)]
    ]

    epoch = 22
    # Layer 1
    positionList = [(1, 1, 7), (15, 1, 7), (1, 15, 7)]
    for i in positionList:
        drawBlock(0, epoch * i[2], (-250 + epoch * i[0], 250 - epoch * i[1]))
    for i in range(23):
        for j in range(23):
            if Matrix[i][j] == 1:
                drawBlock(0, epoch * 1, (-250 + epoch * j, 250 - epoch * i))
    # Layer2
    positionList = [(2, 2, 5), (16, 2, 5), (2, 16, 5)]
    for i in positionList:
        drawBlock(1, epoch * i[2], (-250 + epoch * i[0], 250 - epoch * i[1]))
    # Layer3
    positionList = [(3, 3, 3), (17, 3, 3), (3, 17, 3)]
    for i in positionList:
        drawBlock(0, epoch * i[2], (-250 + epoch * i[0], 250 - epoch * i[1]))
    turtle.goto(-200, 260)
    turtle.write('Simple is better than complex.')
    turtle.done()


# the main function
if __name__ == '__main__':
    t0 = time.time()
    turtle.setup(600, 600)
    # turtle.Turtle().screen.delay(0)
    turtle.speed(0)
    turtle.hideturtle()
    picDraw()
    # exDraw()
