import random

words = [
    ['guess', 'the', 'word'],
    ['sponge', 'bob', 'square'],
    ['how', 'you', 'doing?'],
    ['we', 'love', 'pizza']
]

index = random.randrange(0, len(words))
sen = words[index]

print(sen)
guess = []
for word in sen:
    guess.append('_' * len(word))

print(guess)
