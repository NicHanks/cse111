from datetime import datetime

def get_lunch_time(lunch_time):
    if lunch_time == datetime.now():
        return "It's lunch time! "