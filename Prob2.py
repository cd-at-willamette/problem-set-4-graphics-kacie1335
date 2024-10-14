########################################
# Name: Kassandra Carrasco
# Collaborators:
# Estimated time spent (hrs):
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)
    brick_x =(WIDTH)/2
    brick_y = 400

    # You got it from here
    brick = GRect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
    BRICKS_IN_BASE =15  
    
    while BRICKS_IN_BASE > 0:
        for i in range(BRICKS_IN_BASE):
            gw.add(brick)
        BRICKS_IN_BASE -= 1
        brick_y -= BRICK_HEIGHT 
















if __name__ == '__main__':
    draw_pyramid()
