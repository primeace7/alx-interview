#!/usr/bin/python3
"""Implementation of solution for the minimum operations problem."""


from typing import Any, List
from math import sqrt


def minOperations(n: Any) -> int:
    """Calculate and return the minimum number of opertions to result in n
    characters in a file if only copy and paste operations are possible
    """
    if type(n) is not int or n < 2:
        return 0

    factors: List = []
    get_factors(n, factors)
    return sum(factors)


def get_factors(n: int, result: List):
    """Return the prime factors of a given input number"""
    if n < 2:
        return result
    root = int(sqrt(n)) + 2

    for i in range(2, root):
        if n % i == 0:
            result.append(i)
            return get_factors(n // i, result)
    return result.append(n)
