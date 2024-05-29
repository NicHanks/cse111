
import tkinter as tk
import number_entry as nent

# Next week I will add test functions.

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Fluid Intake per Day")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create labels for the text fields and the results.
    #lbl_width = tk.Label(frm_main, text="Width (mm):")
    lbl_weight = tk.Label(frm_main, text="Weight (in lbs):")
    #lbl_ratio = tk.Label(frm_main, text="Aspect Ratio:")
    lbl_exercise = tk.Label(frm_main, text="Time spent exercising per day (in min):")
    #lbl_diam = tk.Label(frm_main, text="Diameter (in):")
    lbl_climate = tk.Label(frm_main, text="Climate (tropical=1, temperate=2, or cold=3):")
    #lbl_vol = tk.Label(frm_main, text="Volume (liters):")
    lbl_total = tk.Label(frm_main, text="Total amount of water needed per day:")


    # Create three text fields.
    ent_weight = nent.IntEntry(frm_main, 80, 300, width=5)
    ent_exercise = nent.FloatEntry(frm_main, 30, 90, width=5)
    ent_climate = nent.FloatEntry(frm_main, 10, 30, width=5)

    # Create a label to display the result.
    lbl_result = tk.Label(frm_main, width=8, anchor="w")

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, text fields, and buttons in a grid.
    lbl_weight.grid( row=0, column=0, padx=3, pady=2, sticky="e")
    ent_weight.grid( row=0, column=1, padx=3, pady=2, sticky="w")
    lbl_exercise.grid( row=1, column=0, padx=3, pady=2, sticky="e")
    ent_exercise.grid( row=1, column=1, padx=3, pady=2, sticky="w")
    lbl_climate.grid(  row=2, column=0, padx=3, pady=2, sticky="e")
    ent_climate.grid(  row=2, column=1, padx=3, pady=2, sticky="w")
    lbl_total.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
    lbl_result.grid(row=3, column=1, padx=3, pady=2, sticky="w")
    btn_clear.grid( row=3, column=2, padx=3, pady=2)


    # This function is called each time the user releases a key.
    def calculate(event):
        """Compute the approximate volume of water in ."""
        try:
            # Get the user input.
            weight = ent_weight.get()

            # This calls all calculating funcitons...
            weight_total = get_weight_total()
            exercise_total = get_exercise_total(weight_total)
            grand_total = get_climate_total(exercise_total)

            # This displays the grand total!
            lbl_result.config(text=f"{grand_total:.2f}")

        except ValueError:
            # When the user deletes all the digits in one
            # of the text fields, clear the result labels.
            lbl_result.config(text="")


    # This function is called each time
    # the user clicks the "Clear" button.
    def get_weight_total():
        """this gets the total from the weight * magic number"""
        try:
            # this gets the user input
            weight = ent_weight.get()
            total = weight * .5
        except KeyError:
            print(KeyError)
        return total

    def get_exercise_total(total):
        """this gets the new total from weight and exercise"""
        exercise = ent_exercise.get()
        exercise_amount = (exercise/30 * 12)
        new_total = exercise_amount + total
        return new_total
    
    def get_climate_total(total):
        """this gets the total from the exercise total and climate"""
            #77 ounces, 326 ounces -tropical 1.0516129
            #85 ounces, 310 ounces -intermediate
            #93 ounces, 318 ounces -cold 1.02580645
        climate = ent_climate.get()
        try:
            if climate == 1:
                new_total = total * 1.0516129
            elif climate == 2:
                new_total = total * 1
            elif climate == 3:
                new_total = total * 1.02580645
            else:
                print("please hit 'clear' and try agian")
        except KeyError:
            print(f"Sorry, there is a {KeyError}. Please try again")
        return new_total

    def clear():
        """Clear all the inputs and outputs."""
        ent_weight.delete(0, tk.END)
        ent_exercise.delete(0, tk.END)
        ent_climate.delete(0, tk.END)
        lbl_result.config(text="")
        ent_weight.focus()


    # Bind the calculate function to the three text fields
    # so that the calculate function will be called when
    # the user changes the text in the text fields.
    ent_weight.bind("<KeyRelease>", calculate)
    ent_exercise.bind("<KeyRelease>", calculate)
    ent_climate.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the width text field.
    ent_weight.focus()


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()