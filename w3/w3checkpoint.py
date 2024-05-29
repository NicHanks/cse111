def main ():
    # Get an odometer value in U.S. miles from the user.
    start = float(input("What did the odometer start at in miles? "))
    # Get another odometer value in U.S. miles from the user.
    end = float(input("What did the odometer end at in miles? "))
    # Get a fuel amount in U.S. gallons from the user.
    gallons = float(input("How many gallons of fuel was used? "))
    # Call the miles_per_gallon function and store
    mpg = miles_per_gallon(end, start, gallons)
    # the result in a variable named mpg.
    lp100k = lp100k_from_mpg(mpg)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
    # Display the results for the user to see.
    pass

def miles_per_gallon(end, start, gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = (end - start) / gallons
    return mpg

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg
    return lp100k

# Call the main function so that
# this program will start executing.
main()