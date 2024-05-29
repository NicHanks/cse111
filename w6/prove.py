"""During this prove milestone, you will write and test functions that generate sentences with three parts:
1. a determiner (sometimes known as an article)
2. a noun
3. a verb

A cat laughed.
One man eats.
The woman will think.
Some girls thought.
Many dogs run.
Many men will write.
"""
import random

def main():
    quantity = int(input("How many? "))
    tense = input("What is the tense?(past, present, or future) ")
    importance = input("How important is this? (yes/no) ")
    importance = importance.lower
    
    word1 = get_determiner(quantity)
    word2 = get_noun(quantity)
    word3 = get_verb(quantity, tense)
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity)
    punctuation = get_punctuation(importance)

    "each must have a determiner, a noun, a verb, and a prepositional phrase"
    print(f"{word1} {word2} {word3} {prepositional_phrase}{punctuation}")
    word1 = get_determiner(quantity)
    word2 = get_noun(quantity)
    word3 = get_verb(quantity, tense)
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity)
    print(f"{word1} {word2} {word3} {prepositional_phrase}{punctuation}")
    word1 = get_determiner(quantity)
    word2 = get_noun(quantity)
    word3 = get_verb(quantity, tense)
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity)
    print(f"{word1} {word2} {word3} {prepositional_phrase}{punctuation}")
    word1 = get_determiner(quantity)
    word2 = get_noun(quantity)
    word3 = get_verb(quantity, tense)
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity)
    print(f"{word1} {word2} {word3} {prepositional_phrase}{punctuation}")
    word1 = get_determiner(quantity)
    word2 = get_noun(quantity)
    word3 = get_verb(quantity, tense)
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity)
    print(f"{word1} {word2} {word3} {prepositional_phrase}{punctuation}")
    word1 = get_determiner(quantity)
    word2 = get_noun(quantity)
    word3 = get_verb(quantity, tense)
    preposition = get_preposition()
    prepositional_phrase = get_prepositional_phrase(quantity)
    print(f"{word1} {word2} {word3} {prepositional_phrase}{punctuation}")



def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
    
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    return word

    #    #would this work instead?
    #if quantity == 1:
    #    return random["bird", "boy", "car", "cat", "child",
    #    "dog", "girl", "man", "rabbit", "woman"]
    #else:
    #    return random?.choice?["birds", "boys", "cars", "cats", "children",
    #    "dogs", "girls", "men", "rabbits", "women"]

def get_verb(tense, quantity=0):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    #tense = tense.lower()
    verb = "word"
    if tense == "past" and quantity == 0:
        verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    else: #tense == "future":
        verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]


    return random.choice(verb)

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    word1 = get_preposition()
    word2 = get_noun(quantity)
    word3 = get_determiner(quantity)
    prepositional_phrase = f"{word1} {word2} {word3}"
    return prepositional_phrase 

def get_punctuation(importance):
    if importance == "yes":
        punctuation = "!"
    else:
        punctuation = "."
    return punctuation

if __name__ == "__main__":
    main()
