#!/usr/bin/python3
'''Create a utf8 validator function'''
from typing import List


def getspan(data: str) -> int:
    '''Return the number of bytes needed to represent
    a given utf8 codepoint, given the first byte as input
    as a binary string. e.g given input of data = 11101100
    return 3
    '''

    count = 0
    for i in data:
        if i == '1':
            count += 1
        else:
            return count


def validate(data: List) -> bool:
    '''Determine if input list is valid utf8'''
    for i in range(len(data)):
        span = getspan(data[i])
        # below conditionals identify incorrectly encoded binary strings
        if span == 1:
            return False
        elif span and len(data[i:]) < span:
            return False

        for j in range(1, span):
            if data[i + j][:2] != '10':
                return False
        if span:
            i += span
    return True


def validUTF8(data: List) -> bool:
    '''Determine if input data has valid utf8 encoding'''
    if len(data) == 0:
        return False

    code = []
    for num in data:
        binary = bin(num)[2:]
        binary = binary if len(binary) > 7 else '0' + binary
        code.append(binary)

    return validate(code)
