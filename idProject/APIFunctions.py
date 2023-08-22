import requests


def check_special_chars(url, word):
    res = requests.get(url + word)
    return 'program' in res.text and res.status_code < 400


def register(url, data):
    res = requests.post(url, json=data)
    return res.status_code, res.json()


def check_valid_country(url, country, postalcode):
    res = requests.get(f'{url}/{country}/{postalcode}')
    if res.status_code < 400:
        return res.json()['country']
