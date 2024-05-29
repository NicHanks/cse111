import random


def main():
    numbers = [16.2, 75.1, 52.3] 
    quantity = 2
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    words_list = []
    append_random_words(words_list, 3)
    print(words_list)
    
def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        number = random.uniform(0, 100)
        number = round(number, 1)
        numbers_list.append(number)
def append_random_words(words_list, quantity=1):
    words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    for i in range(quantity):
        word = random.choice(words)
        words_list.append(word)


if __name__ == "__main__":
    main()