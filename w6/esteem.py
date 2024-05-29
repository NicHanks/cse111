def main():
    index = 1
    total = 0

    user = input("I feel that I am a person of worth, at least on anequal plane with others.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("I feel that I have a number of good qualities.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("All in all, I am inclined to feel that I am a failure.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("I am able to do things as well as most other people.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("I feel I do not have much to be proud of.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("I take a positive attitude toward myself.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("On the whole, I am satisfied with myself.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("I wish I could have more respect for myself.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("I certainly feel useless at times.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)
    index += 1

    user = input("At times I think I am no good at all.\n Enter D, d, a, or A: ")
    total = total + get_score(index, user)

    print(f'Your score is {total}.')
    print('A score below 15 may indicate problematic low self-esteem.')
    

def get_score(quest_num, user_responds):
    if quest_num == 1 or quest_num == 2 or quest_num == 4 or quest_num == 6 or quest_num == 7:

        return get_positive(user_responds)
    else:
        return get_negative(user_responds)


def get_positive(user_responds):
    if user_responds == "D":
        return 0
    elif user_responds == "d":
        return 1
    elif user_responds == "a":
        return 2
    elif user_responds == "A":
        return 3

def get_negative(user_responds):
    if user_responds == "D":
        return 3
    elif user_responds == "d":
        return 2
    elif user_responds == "a":
        return 1
    elif user_responds == "A":
        return 0

main()
"""
def main():
    
    list = ["I feel that I am a person of worth, at least on an equal plane with others.",
    "I feel that I have a number of good qualities.",
    "All in all, I am inclined to feel that I am a failure.",
    "I am able to do things as well as most other people.",
    "I feel I do not have much to be proud of.",
    "I take a positive attitude toward myself.",
    "On the whole, I am satisfied with myself.",
    "I wish I could have more respect for myself.",
    "I certainly feel useless at times.",
    "At times I think I am no good at all.",]

    for _ in range.len(list):
        print (list)

def get_score(first, second):
    if quest_num == 1 or 2 or 4 or 6 or 7:

    if 
"""