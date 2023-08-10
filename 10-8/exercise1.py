# pip install requests

import requests

random_joke_url = 'https://api.chucknorris.io/jokes/random'
categories_url = 'https://api.chucknorris.io/jokes/categories'
joke_by_categoru_url = 'https://api.chucknorris.io/jokes/search?query='


def get_joke(url):
    '''
    :param url:  the url to send http get request
    :return:  json of the api
    '''
    res = requests.get(random_joke_url)
    if res.status_code < 400:
        joke = res.json()
        return joke


# get_joke(random_joke_url)

def get_categories(url):
    '''

    :param url: the url to receive the list of categories
    :return:  to return list of categories
    '''
    res = requests.get(categories_url) # send http request
    categories = res.json() # convert the list into python list
    return categories


categories = get_categories(categories_url)
joke = get_joke(joke_by_categoru_url + categories[2]) # get joke by the third category
print(joke)
