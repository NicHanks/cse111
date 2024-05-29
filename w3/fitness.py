from datetime import datetime

def main():
    gender = input(f"Please enter your gender (M or F): ")
    gender = gender.lower()
    born_str = input(f"Enter your birthdate (YYYY-MM-DD): ")
    weight = float(input(f"Enter your weight in U.S. pounds: "))
    height = float(input(f"Enter your height in U.S. inches: "))

    age = calculate_age(born_str)
    #bmi = body_mass_index(weight, height)
    #bmr = basal_metabolic_rate(weight, height, age)

    print(f"Age (years): {calculate_age(born_str)}")
    print(f"Weight (kg): {kg_from_lb(weight):.2f}")
    print(f"Height (cm): {cm_from_in(height)}")
    print(f"Body mass index: {body_mass_index(weight, height):.2f}")
    print(f"Basal metabolic rate (kcal/day): {basal_metabolic_rate(gender, weight, height, age):.0f}")

def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg

def cm_from_in(height):
    return height * 2.54

def calculate_age(born_str):
    born = datetime.strptime(born_str, "%Y-%m-%d")
    today = datetime.today()
    #born = datetime(born)
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    

def body_mass_index(weight, height):
    '''Finding Body Mass Index (BMI)'''
    return (10000 * weight) / (height ** 2)

def basal_metabolic_rate(gender, weight, height, age):
    '''finding basal metablic rate'''
    if gender == "f":
        #female bmr
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        #male bmr
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

main()