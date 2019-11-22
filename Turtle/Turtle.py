from turtle import *
answer = input('Enter length of polygon sides: ')
side_length = int(answer)
answer = input('Enter number of sides of polygon: ')
sides = int(answer)
angle = 360/sides
answer = input('Enter number of polygons: ')
polygons = int(answer)
rotation = 360/polygons
colour_index = 0
speed(0)
for polygon in range(polygons):
    if colour_index == 0:
        color('red')
    if colour_index == 1:
        color('green')
    if colour_index == 2:
        color('blue')
    for side in range(sides):
        forward(side_length)
        right(angle)
    colour_index = colour_index + 1
    if colour_index == 3:
        colour_index = 0
    right(rotation)
    f = input()