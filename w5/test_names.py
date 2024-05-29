from names import make_full_name, \
    extract_family_name, extract_given_name
from address import extract_city, extract_state, extract_zipcode
import pytest

def test_make_full_name():
    #assert make_full_name("Oscar", "Perez") == "Perez; Oscar"
    #assert make_full_name("", "Perez") == "Perez; Oscar"
    #assert make_full_name("", "") == "Perez; Oscar"
    assert make_full_name("Oscar", "Perez") == "Perez; Oscar"
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("Olivier", "Toussaint") == "Toussaint; Olivier"
    assert make_full_name("George", "Washington") == "Washington; George"
    assert make_full_name("Martha", "Washington") == "Washington; Martha"

def test_extract_family_name():
    #assert extract_family_name("Oscar", "Perez") == "Perez"
    #assert extract_family_name("Oscar", "Perez") == "Perez"
    assert extract_family_name("Toussaint; Marie") == "Toussaint"
    assert extract_family_name("Toussaint; Oliver") == "Toussaint"
    assert extract_family_name("Washington; George") == "Washington"
    assert extract_family_name("Washington; Martha") == "Washington"

def test_extract_given_name():
    #assert extract_given_name("Oscar", "Perez") == "Oscar"
    #assert extract_given_name("Maria", "Perez") == "Maria"
    assert extract_given_name("Marie", "Toussaint") == "Marie"
    assert extract_given_name("Olivier", "Toussaint") == "Olivier"
    assert extract_given_name("George", "Washington") == "George"
    assert extract_given_name("Martha", "Washington") == "Martha"

# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
Verify that the extract_city, extract_state,
and extract_zipcode functions work correctly.
"""

def test_extract_city():
    """Verify that the extract_city function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    assert extract_city("78 Pine St, Avon Park, FL 33825") == "Avon Park"


def test_extract_state():
    """Verify that the extract_state function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert extract_state("123 W Main, Rexburg, ID 83440") == "ID"
    assert extract_state("78 Pine St, Avon Park, FL 33825") == "FL"


def test_extract_zipcode():
    """Verify that the extract_zipcode
    function returns correct results.

    Parameters: none
    Return: nothing
    """
    assert extract_zipcode("123 W Main, Rexburg, ID 83440") == "83440"
    assert extract_zipcode("78 Pine St, Avon Park, FL 33825") == "33825"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
