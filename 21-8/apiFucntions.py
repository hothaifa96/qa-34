import requests


def get_all_facts(url):
    res = requests.get(url + 'facts')  # fires the request to the given url and retrieve dat
    if res.status_code < 400:
        data = res.json()
    return data['data']


def get_status(url):
    res = requests.get(url)  # fires the request to the given url and retrieve dat
    return res.status_code


def get_one_fact(url):
    res = requests.get(url + 'fact')  # fires the request to the given url and retrieve dat
    if res.status_code < 400:
        data = res.json()
    return data['fact']


def get_response(url):
    try:
        res = requests.get(url)
        if res.status_code >= 400:
            raise Exception('not a valid status')
        return res
    except:
        return None
