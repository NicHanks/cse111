
import pytest
from pytest import approx
import water_intake
import tkinter as tk
import number_entry as nent

def test_get_weight_total():
    variable = water_intake.populate_main_window.get_weight_total(200)
    #total = 200 * .5
    assert variable == 100
    variable = water_intake.populate_main_window.get_weight_total(150)
    #total1 = 150 * .5
    assert variable == 75

def test_get_exercise_total():
    variable1 = water_intake.populate_main_window.get_exercise_total(30)
    #total = (variable1/30 * 12)
    assert variable1 == 12
    variable2 = water_intake.populate_main_window.get_exercise_total(60)
    #total = (variable2/30 * 12)
    assert variable2 == 24

def test_get_weight_total():
    variable = water_intake.populate_main_window.get_climate_total(1)
    total = (variable * 1.0516129)
    assert variable == total
    variable = water_intake.populate_main_window.get_climate_total(2)
    total2 = (variable * 1)
    assert variable == total2
    variable = water_intake.populate_main_window.get_climate_total(3)
    total3 = (variable * 1.02580645)
    assert variable == total3

