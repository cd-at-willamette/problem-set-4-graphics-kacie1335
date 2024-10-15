########################################
# Name: Kassandra Carrasco
# Collaborators:
# Estimate time spent (hrs):3
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
total = 0

gw = GWindow(GW_WIDTH, GW_HEIGHT)

square = GRect(SQUARE_SIZE, SQUARE_SIZE)
square.set_filled(True)
square.set_color("pink")

gw.add(square, GW_WIDTH/2, GW_HEIGHT/2)
score = GLabel(str(0))

gw.add(score, 0 , GW_HEIGHT)

def clicky_box():

    
    # Defining the callback function, which you won't need until Part C
    def on_mouse_click(event):
        if square.contains(event.get_x(), event.get_y()):
            square.set_location(random.randint(0,(GW_WIDTH - SQUARE_SIZE)), random.randint(0,(GW_WIDTH - SQUARE_SIZE)))
            score.set_label(str(int(score.get_label())+1))
        else:
            score.set_label(str(0))
    
    gw.add_event_listener("click", on_mouse_click)







if __name__ == '__main__':
    clicky_box()
