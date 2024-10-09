############################################################
# Name: Kassandra Carrasco
# Name(s) of anyone worked with:
# Est time spent (hr):1
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    w= 400

    #green box
    r = GRect(w//1,w)
    r.set_filled(True)
    r.set_fill_color("Green")
    gw.add(r)

    #pink oval petals
    o = GOval(200,100,60,60)
    o.set_filled(True)
    o.set_fill_color("Pink")
    gw.add(o)

    o = GOval(200,150,60,60)
    o.set_filled(True)
    o.set_fill_color("Pink")
    gw.add(o)

    o = GOval(150,150,60,60)
    o.set_filled(True)
    o.set_fill_color("Pink")
    gw.add(o)

    o = GOval(150,100,60,60)
    o.set_filled(True)
    o.set_fill_color("Pink")
    gw.add(o)

    #yellow oval 
    o = GOval(180,130,50,50)
    o.set_filled(True)
    o.set_fill_color("Yellow")
    gw.add(o)



    gw.add(GLine(200,200,200,400))

    gw.add(GLabel("flower", 300, w//2))
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!





if __name__ == '__main__':
    draw_image()

