
instructions = [(l[0], int(l[1:])) for l in open("input")]

ship_x = 0
ship_y = 0
wp_x = 10
wp_y = 1
d = 1
#              0   1   2   3
directions = ["N","E","S","W"]


def change_dir(degree):
    degree = degree/90
    return (d+degree) % 4

def rotate_wp(angle):
    angle = angle/90

    global wp_x
    global wp_y

    if angle == 1:
        # 2 1 => 1 -2
        temp = wp_x
        wp_x = wp_y
        wp_y = -temp

    elif angle == 2:
        wp_x = -wp_x
        wp_y = -wp_y
    elif angle == 3:
        # 2 1 => -1 2
        temp = wp_y
        wp_y = wp_x
        wp_x = -temp
    
    return wp_x, wp_y


for inst, val in instructions:
    if inst == "N":
        wp_y+=val
    elif inst == "S":
        wp_y-=val
    elif inst == "W":
        wp_x-=val
    elif inst == "E":
        wp_x+=val
    elif inst == "F":
        ship_x+=val*wp_x
        ship_y+=val*wp_y

    elif inst == "R":
        wp_x, wp_y = rotate_wp(val)
    elif inst == "L":
        wp_x, wp_y = rotate_wp(360 - val)



print(abs(ship_x)+abs(ship_y))




