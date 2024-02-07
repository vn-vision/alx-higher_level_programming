#!/usr/bin/python3
""" script that reads stdin line by line
and computes metrics """
import sys


tt_size = 0
status_cnt = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
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

            if status_code in status_cnt:
                status_cnt[status_code] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(tt_size))
            for code in sorted(status_cnt.keys()):
                if status_cnt[code] > 0:
                    print("{}: {}".format(code, status_cnt[code]))

except KeyboardInterrupt:
    """ this handles keyboard interractions """

    print("File size: {}".format(tt_size))
    for code in sorted(status_cnt.keys()):
        if status_cnt[code] > 0:
            print("{}: {}".format(code, status_cnt[code]))
    sys.exit(0)
