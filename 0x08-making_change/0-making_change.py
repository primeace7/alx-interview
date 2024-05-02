#!/usr/bin/python3
'''Implementation of the coin change problem solution'''
from typing import List


def makeChange(coins: List, total: int) -> int:
    '''Compute and return the least quantity of coins
    to make up a given amount, i.e total.
    '''
    if total <= 0:
        return 0
    elif total < min(coins):
        return -1

    min_val = min(coins)
    tracker = {i: -1 for i in range(min_val, total + 1)}

    for i in range(min_val, total + 1):
        outcomes = []
        for coin in coins:
            remain = i - coin
            if remain < 0:
                continue
            elif remain and remain < min_val:
                continue
            elif remain == 0:
                outcomes.append(1)
            else:
                if tracker[remain] == -1:
                    continue
                else:
                    outcomes.append(tracker[remain] + 1)
        if len(outcomes) > 0:
            tracker[i] = min(outcomes)

    return tracker[total]
