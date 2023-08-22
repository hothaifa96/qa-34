import pytest
from APIFunctions import *


class TestAPI:
    @pytest.fixture()
    def url(self):
        return 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    @pytest.mark.parametrize('word', [("C++"), ("++C"), ("+C+"), ("C+C"), ("!!@$")])
    def test1_special_chars(self, url, word):
        actual = check_special_chars(url, word)  # True / False
        assert actual, 'do not support special chars'


class TestReqResAPI:

    def test1_register_P(self, url='https://reqres.in/api/register'):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        status_code, token = register(url, data)
        assert status_code < 400 and token is not None, 'bad cred'

    def test2_register_N(self, url='https://reqres.in/api/register'):
        data = {
            "email": "roni@reqres.in",
            "password": "pistol"
        }
        status_code, token = register(url, data)
        assert status_code >= 400 or token is None


class TestZipAPI:
    def test_canada_zipcode(self):
        actual = check_valid_country('https://api.zippopotam.us', 'US', 'K1A')
        assert 'canada' in actual.lower()
