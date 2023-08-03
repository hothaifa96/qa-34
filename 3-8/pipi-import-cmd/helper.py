# print hi length of your name times
def say_hi(name: str):
    '''
    this function print hi
    :param name: user name
    :return: void
    '''
    for n in name:
        print(f'{n}) hi')


def day_in_week(day):
    week = {0: 'sat',
            1: 'sun',
            2: 'mon',
            3: 'tue',
            4: 'wed',
            5: 'thu',
            6: 'fri'}
    print(week[day % 7])


def star(n):
    for i in range(1, n):
        print(' ' * (n - i), '* ' * i)
    for i in range(n, 0, -1):
        print(' ' * (n - i), '* ' * i)



age = 34

if __name__ == '__main__':
    star(5)
