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
    i = 0
    while i < len(data):
        span = getspan(data[i])
        # below conditionals identify incorrectly encoded binary strings
        if span == 1:
            return False
        elif span and len(data[i:]) < span:
            return False

        for j in range(1, span):
            if data[i + j][:2] != '10':
                return False
        i += span if span else 1
    return True

def encode(data: List) -> List:
    '''encode a list of ints into binary with correct number
    of unicode bytes. e.g 467 should be encoded in 2 bytes
    i.e 16 bits, instead of 9 as returned by bin()
    '''
    encoding = []
    for num in data:
        binary = bin(num)[2:]
        count = len(binary)
        if count % 8:
            extra = '0' * (8 * ((count // 8) + 1) - count)
            binstring = extra + binary
            for i in range(len(binstring) // 8):
                idx = i * 8
                encoding.append(binstring[idx: idx + 8])
        else:
            encoding.append(binary)
    return encoding

def validUTF8(data: List) -> bool:
    '''Determine if input data has valid utf8 encoding'''
    if len(data) == 0:
        return False

    code = encode(data)
    return validate(code)
