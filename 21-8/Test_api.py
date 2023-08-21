import pytest
from apiFucntions import *


class Test_cat_fact:
    @pytest.fixture()
    def url(self):
        return 'https://catfact.ninja/'

    def test1_check_status_fact(self, url):
        fact = get_status(url + 'fact')
        assert 200 <= fact < 400

    def test2_check_one_fact(self, url):
        actual = get_one_fact(url)

        assert len(actual) > 0

    def test3_check_cat_in_response(self, url):
        actual = get_response('https://google.com')
        assert actual != None
