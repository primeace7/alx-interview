#!/usr/bin/python3
'''parse web server logs to extract stats of http response codes'''

import sys
import re
recorder = [0, {}, 0]

date_re = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[.]\d{6}\]'
ip_re = r'^\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3} - '
http_re = r' "GET /projects/260 HTTP/1.1" '
http_code_re = r'(\d{3}) (\d+)$'
expression = ip_re + date_re + http_re + http_code_re

regex = re.compile(expression)


def parse_line(line: str) -> None:
    '''parse a single line of web server log to extract
    neccessary data
    '''
    match = regex.match(line)
    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))
        recorder[0] += 1
        if status_code in recorder[1]:
            recorder[1][status_code] += 1
        else:
            recorder[1][status_code] = 1
        recorder[2] += file_size


def print_records() -> None:
    '''print all extracted stats from analysed log'''
    print(f'File size: {recorder[2]}')
    for key in recorder[1].keys():
        print(f'{key}: {recorder[1][key]}')


try:
    for line in sys.stdin:
        parse_line(line)
        if recorder[0] and recorder[0] % 10 == 0:
            print_records()
except KeyboardInterrupt:
    print_records()
    raise
