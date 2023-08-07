import requests

url = 'https://cars-uog6.onrender.com/cars'


# GETALL GETBYID DELETE PUT POST

# GET ALL CARS
def get_all_cars(url):
    res = requests.get(url)
    if res.status_code < 400:
        data = res.json()
        return data
    else:
        return None


def get_car_by_id(url, id):
    res = requests.get(f'{url}/{id}')
    if res.status_code < 400:
        car = res.json()
        return car


# print(get_car_by_id(url, 8))

def delete_car(url, id):
    res = requests.delete(f'{url}/{id}')
    return res.status_code < 400


# print(delete_car(url, 3))

def add_car(url):
    new_car = {'make': input('enter make'),
               'model': input('enter model'),
               'year': int(input('enter year'))}

    res = requests.post(url, json=new_car)
    if res.status_code < 400:
        print('Done')


# add_car(url)

# res = requests.patch(f'{url}/{2}', data={'year':2010})
# print(res.status_code)

