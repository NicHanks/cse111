#python tire_volume.py

import math
from tkinter import N

w = float(input("Enter the width of the tire in mm (ex 205): ")) #185
a = float(input("Enter the aspect ratio of the tire (ex 60): ")) #50
d = float(input("Enter the diameter of the wheel in inches (ex 15): ")) #14
brand = input("What is the brand of the tire? ")

volume = (math.pi * w**2 * a *(w * a + 2540 * d)) / 10000000000
volume = round(volume, 2)
print("The brand '", brand, "' holds approximately: ", volume, " liters.")

from datetime import datetime
current_date = datetime.now()
with open("volumes.txt", "at") as volume_file:
    print(current_date, w, a, d, volume, file=volume_file)

print("Here is the website")
import time
x = 0
while x != 3:
    time.sleep(.5)
    print("Here is the website.")
    time.sleep(.5)
    print("Here is the website..")
    time.sleep(.5)
    print("Here is the website...")
    x = x + 1
import webbrowser
webbrowser.open("http://www.", brand, ".com")