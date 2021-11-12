import pytest
from temperature import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
	assert celsius_to_fahrenheit(21) == 69.8

def test_celsius_to_fahrenheit_equivlance_point():
	assert celsius_to_fahrenheit(-40) == -40

def test_celsius_to_fahrenheit_float():
	assert celsius_to_fahrenheit(21.2) == 70.16

def test_celsius_to_fahrenheit_string():
	with pytest.raises(TypeError):
		f = celsius_to_fahrenheit("21")