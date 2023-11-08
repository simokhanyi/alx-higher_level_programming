#!/usr/bin/python3
"""
Metrics script that reads stdin line by line and computes statistics.
"""


import sys
from collections import defaultdict


def print_metrics(metrics):
    print("Total file size: File size: {}".format(metrics['total_size']))
    for status_code in sorted(metrics['status_codes']):
        count = metrics['status_codes'][status_code]
        if count > 0:
            print("{}: {}".format(status_code, count))


def main():
    metrics = {
        'total_size': 0,
        'status_codes': defaultdict(int)
    }

    try:
        line_count = 0
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 7:
                status_code = parts[-2]
                try:
                    file_size = int(parts[-1])
                except ValueError:
                    file_size = 0

                metrics['total_size'] += file_size
                metrics['status_codes'][status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_metrics(metrics)

    except KeyboardInterrupt:
        print_metrics(metrics)


if __name__ == "__main__":
    main()
