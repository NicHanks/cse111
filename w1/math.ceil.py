# How to use math.ceil
import math

items = float(input("Enter the number of items: "))
boxes = float(input("Enter the number of items per box: "))

print("For ", items," items, packing ", boxes," items in each box, you will need ", math.ceil(items/boxes), " boxes.")
