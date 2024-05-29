# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from w4draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    horizen = 300

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_grid(canvas, scene_width, scene_height, 50)
    draw_sky(canvas, scene_width, scene_height, horizen)
    draw_sun(canvas, scene_width, scene_height)
    draw_cloud(canvas, scene_width, scene_height, 0)
    draw_cloud2(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height, horizen)
    draw_grass(canvas,scene_width, scene_height)

    #draw_sky()

    #draw_ground()

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval):
    for_label_y = 10
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        #draw_text(canvas, x, 0, for_label_y, f"{x}")
    
    for_label_x = 10
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        #draw_text(canvas, 0, y, for_label_x, f"{y}")

def draw_sky(canvas, width, height, interval, color="light blue"):
    draw_rectangle(canvas, width, height, 0, interval, fill=color)

def draw_cloud(canvas, width, height, interval, color="white"):
    x = width * .17
    y = height - 75
    diameter = 150
    diametery = 50
    draw_oval(canvas, x, y, x + diameter, y + diametery, fill=color)
def draw_cloud2(canvas, width, height):
    color = "white"
    draw_oval(canvas, width * .5, height * .87, width * .95, height *.97, fill=color)
def draw_sun(canvas, scene_width, scene_height, color="yellow"):
    draw_oval(canvas, 700, 400, 25, 25, fill=color)

def draw_ground(canvas, scene_width, height, horizen, color="green"):
    draw_line(canvas, 0, horizen, scene_width, horizen)
    draw_rectangle(canvas, 0, 0, scene_width, 300, fill=color)

def draw_grass(canvas, scene_width, scene_height):
    for i in range(0,scene_width,20):
        color = "green"
        draw_rectangle(canvas, i, 100,i +10, 115, fill=color)
        #draw_polygon(canvas, i,100,i+10 100,i+10,115,i+7,117,i,115,*coords: Any, width = int 1, line = str "green", fill = str"green")
        color = "dark green"
        draw_rectangle(canvas, i +10, 100, i +20, 115, fill=color)
    for i in range(0,scene_width,20):
        color = "dark green"
        draw_rectangle(canvas, i, 80,i +10, 100, fill=color)
        color = "green"
        draw_rectangle(canvas, i +10, 80, i +20, 100, fill=color)
    for i in range(0,scene_width,20):
        color = "green"
        draw_rectangle(canvas, i, 50,i +10, 80, fill=color)
        color = "dark green"
        draw_rectangle(canvas, i +10, 50, i +20, 80, fill=color)
    for i in range(0,scene_width,20):
        color = "dark green"
        draw_rectangle(canvas, i, 0,i +10, 50, fill=color)
        color = "green"
        draw_rectangle(canvas, i +10, 0, i +20, 50, fill=color)




#def draw_sky():

#def draw_ground():

# Call the main function so that
# this program will start executing.
main()