#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    """
    Prints the statistics based on total file size and status codes.

    :param total_size: Total file size.
    :type total_size: int
    :param status_codes: A dictionary containing status codes and counts.
    :type status_codes: dict
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    total_size = 0
    status_codes = {str(code): 0 for code in (200, 301, 400, 401, 403, 404, 405, 500)}

    line_number = 0

    for line in sys.stdin:
        line_number += 1
        fields = line.split()
        if len(fields) >= 2:
            status_code = fields[-2]
            file_size = int(fields[-1])
            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

        if line_number % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
