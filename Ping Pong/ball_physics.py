import math


def move_ball(x, y, dx, dy, speed):
    x += speed * dx
    y += speed * dy
    return x, y


def ball_hit(dx, dy, place):
    if place == 'height':
        return dx, -dy
    elif place == 'width':
        return -dx, dy


def hit_screen_height(screen_height, y):
    if y > screen_height or y <= 0:
        return True


def hit_screen_width(screen_width, x):
    if x > screen_width + 20:
        return 1
    elif x <= -20:
        return -1


def shapes_collision(x, y, x2, y2):
    if x == x2 and math.isclose(y - 22, y2, abs_tol=20):
        return True