#!/usr/bin/python3
'''Implementation of Prime Game solution'''


def get_primes(limit):
    '''
    Finds and returns a list of all prime numbers
    less than or equal to limit
    '''
    space = [i for i in range(2, limit + 1)]
    primes = []
    if limit <= 1:
        return primes

    while len(space):
        lowest_prime = space[0]
        primes.append(space[0])
        del space[0]

        for elem in range(lowest_prime ** 2, limit + 1, lowest_prime):
            try:
                del space[space.index(elem)]
            except ValueError:
                continue

    return primes


def isWinner(x, nums):
    '''
    Return one of 'Maria' and 'Ben' as the winner
    of x rounds of the Prime Game where nums is a list of
    the chosen number for each round
    '''
    wins = {'Ben': 0, 'Maria': 0}
    if x == 0 or len(nums) == 0:
        return 'Ben'

    for i in range(x):
        game_round = nums[i]
        primes = get_primes(game_round)

        if len(primes) % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    return 'Maria' if wins['Maria'] > wins['Ben'] else 'Ben'
