#!/usr/bin/python3
""" script that reads stdin line by line
and computes metrics """
import sys


tt_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 1

try:
    """ this handle the display """

    for line in sys.stdin:
        line_count += 1
        token = line.split()
        if len(token) >= 5:
            status_code = int(token[-2])
            f_size = int(token[-1])
            tt_size += f_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(tt_size))
            for code in sorted(status_code_counts.keys()):
                if status_code_counts[code] > 0:
                    print("{}: {}".format(code, status_code_counts[code]))

            tt_size = 0
            status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

except KeyboardInterrupt:
    """ this handles keyboard interractions """

    print("File size: {}".format(tt_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))
    sys.exit(0)
