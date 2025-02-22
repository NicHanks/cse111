# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
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
    draw_cloud(canvas, scene_width, scene_height, 0)
    draw_ground(canvas, scene_width, scene_height, horizen)

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

def draw_cloud(canvas, width, height, interval):
    x = width * .20
    y = height - 75
    diameter = 50
    diametery = 75
    draw_oval(canvas, x, y, x + diameter, y + diametery)

def draw_ground(canvas, width, height, horizen):
    draw_line(canvas, 0, horizen, width, horizen)



#def draw_sky():

#def draw_ground():

# Call the main function so that
# this program will start executing.
main()