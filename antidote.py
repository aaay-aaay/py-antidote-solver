import itertools
import random

def simulate(guess, actual):
    o = 0
    t = 0
    x = 0
    for i, n in enumerate(guess):
        if n == actual[i]:
            t += 1
        elif n in actual:
            o += 1
        else:
            x += 1
    return 'O' * o + '!' * t + 'X' * x

possible = [x[:-1] for x in itertools.permutations('ABCDE')]

print('Antidote Solver')
print('Output is guesses using ABCDE')
print('Input is results using !OX (! = tick)')

while len(possible) > 1:
    guess = random.choice(possible)
    print(''.join(guess))
    res = input()
    if res == '!!!!':
        exit()
    possible = [x for x in possible if simulate(guess, x) == res]
    print(possible)

print(f'Solution: {"".join(possible[0])}')