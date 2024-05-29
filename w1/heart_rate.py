"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

print("Welcome to your heart rate range finder!")

age = int(input("What is your age? "))

max = 220 - age
range1 = max * .65
range2 = max * .85

print("When you exercise to strengthen your heart, you should")
print("keep your heart rate between ", (round(range1))," and ", (round(range2)), " beats per minute.")