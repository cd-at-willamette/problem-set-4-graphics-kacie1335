########################################
# Name: Kassandra Carrasco
# Collaborators:
# Estimated time spent (hrs):2
########################################


from pgl import GWindow, GRect

WIDTH = 1000
HEIGHT = 1000
BRICK_WIDTH = 40
BRICK_HEIGHT = 20   
BRICKS_IN_BASE = 15


gw = GWindow(WIDTH, HEIGHT)

brick_x = WIDTH/2 - ((BRICKS_IN_BASE*BRICK_WIDTH)/2)
brick_y = HEIGHT/2 + ((BRICKS_IN_BASE*BRICK_HEIGHT)/2)

while BRICKS_IN_BASE >=0:
    temp_x = brick_x
    for i in range(BRICKS_IN_BASE):
        gw.add(GRect(temp_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))
        temp_x += BRICK_WIDTH
    BRICKS_IN_BASE -= 1
    brick_y -= BRICK_HEIGHT
    brick_x += (BRICK_WIDTH)/2  





if __name__ == '__main__':
    draw_pyramid()
