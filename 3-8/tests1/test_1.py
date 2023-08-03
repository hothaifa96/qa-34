# *_test.py
# test_*.py
import math
import pytest
import requests


def getname(id):
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    data = res.json()
    return data['name']


@pytest.fixture()
def input_value():
    return 2


@pytest.mark.parametrize('id,expected', [(1, 'Leanne Graham'), (4, 'hodi')])
def test_username_in_get_http(id, expected):
    assert getname(id) == expected


@pytest.mark.parametrize('number', [-2, 0, 2, 4, 8, 199, 56])
def test_even_numbers(number):
    assert number % 2 == 0


@pytest.mark.parametrize('actual,expected', [(144, 12), (81, 9), (169, 13)])
def test_sqrt(actual, expected):
    assert math.sqrt(actual) == expected


def test_power_p(input_value):
    expected = 8
    actual = input_value ** 3
    assert expected == actual


def test_power_n(input_value):
    expected = 9
    actual = input_value ** 3
    assert expected != actual


def test_math_p(input_value):
    expected = input_value ** 2
    actual = math.pow(input_value, 2)
    assert expected == actual
