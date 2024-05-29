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

from string import punctuation
from prove import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_punctuation
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
    verb = 0
    for _ in range(6):
        verb = get_verb("past", 0)
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        assert verb in verbs
    for _ in range(6):
        verb2 = get_verb("present", 1)
        verbs2 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        assert verb2 in verbs2
    for _ in range(6):
        verb3 = get_verb("present", 2)
        verbs3 = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        assert verb3 in verbs3
    for _ in range(6):
        verb4 = get_verb("future", 0)
        verbs4 = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        assert verb4 in verbs4 


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

def test_get_preposition():
    for _ in range(8):
        word = get_preposition()
        words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        assert word in words

def test_get_prepositional_phrase():
    for _ in range(20):
        phrase = get_prepositional_phrase(1)
        words = phrase.split(" ")
        prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        determiner = ["the", "a", "one", "some", "many"]
        for _ in words:
            assert words[0] in prepositions
            assert words[1] in nouns
            assert words[2] in determiner 
    for _ in range(4):
        phrase2 = get_prepositional_phrase(0)
        words = phrase2.split(" ")
        prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        determiner = ["the", "a", "one", "some", "many"]
        for _ in words:
            assert words[0] in prepositions
            assert words[1] in nouns
            assert words[2] in determiner 
        
def test_get_punctuation():
    punctuation = get_punctuation("yes")
    assert punctuation == "!"
    punctuation = get_punctuation("no")
    assert punctuation == "."
    """punctuations = [".", "!", "?"]
    assert punctuation in punctuations"""


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