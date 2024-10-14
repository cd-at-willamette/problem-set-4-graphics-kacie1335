########################################
# Name: Kassandra Carrasco
# Collaborators:
# Estimated time spent (hrs):2
########################################

from pgl import GWindow, GRect

WIDTH = 400
HEIGHT = 400
BRICK_WIDTH = 20
BRICK_HEIGHT = 10
BRICKS_IN_BASE = 15


def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)
    brick_y = 150

    extra_brick = BRICKS_IN_BASE

    # You got it from here 
    
    while extra_brick > 0:

        brick_x = (WIDTH - (extra_brick * BRICK_WIDTH))/2

        for i in range(extra_brick):
            brick = GRect(brick_x + i * BRICK_WIDTH, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
            gw.add(brick)

        brick_y -= BRICK_HEIGHT
        extra_brick -= 1








if __name__ == '__main__':
    draw_pyramid()
