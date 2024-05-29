"""practice
from sentences import main
import random
import pytest 

def test_windshield_function()
    windchill = get_windchill(0,3)
    asset windchill == approx(6.9)

pytest.main(["-v", "--tb=no", "test_weather.py"])

def test_get_determiner():
    # Call the get_determiner function.
    determ = get_determiner(1)

    # Verify that the word stored in the variable
    # determ is in the list of single determiners.
    words = ["a", "one", "the"]
    assert determ in words

def test_get_determiner():
    determ = get_determiner(1)

    words = ["a", "one", "the"]
    assert determ in words
"""

from sentences import get_determiner, get_noun, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    for _ in range(5):
    #for _ in random in range(2):
        noun = get_noun(1)
        #if _ == 1:
        words = ["bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"]
        assert noun in words
    for _ in range(5):
        noun = get_noun(3)
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        assert noun in words

def test_get_verb():
    for _ in range(6):
        verb = get_verb("past", 0)
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        assert verb in verbs
    for _ in range(6):
        verb = get_verb("present", 0)
        verbs2 = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        assert verb in verbs2
    for _ in range(20):
        verb = get_verb("present", 1)
        verbs3 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        assert verb in verbs3
    for _ in range(3):
        verb = get_verb("future", 0)
        verbs4 = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        assert verb in verbs4 


        """if tense == "past":
        verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]"""
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
#practice pytest.main(["-v", "--tb=line", "-rN", __file__])

"""practice
a list is like this:

words = ["hairy", "cat", "froto", "dog"]

word = random.choice(words)

word = "bird"

cap_word = word.capitalize()

from test_sentences import 
"""