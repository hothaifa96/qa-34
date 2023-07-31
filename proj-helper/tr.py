import random


def auto_generate():
    game = open('game.txt', 'w+')
    for n in range(0, 10):
        game.write(str(n) * random.randrange(1, 20))
    game.write('TREATURE')
    for n in range(9, -1, -1):
        game.write(str(n) * random.randrange(1, 20))


auto_generate()
