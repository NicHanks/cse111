#python tire_volume.py

import math

w = float(input("Enter the width of the tire in mm (ex 205): ")) #185
a = float(input("Enter the aspect ratio of the tire (ex 60): ")) #50
d = float(input("Enter the diameter of the wheel in inches (ex 15): ")) #14

volume = (math.pi * w**2 * a *(w * a + 2540 * d)) / 10000000000
volume = round(volume, 2)
print("The approximate volume is ", volume, "liters")
