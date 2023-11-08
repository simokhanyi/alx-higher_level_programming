#!/usr/bin/python3
import sys
import signal


def print_stats(total_size, status_counts):
    """
    Print statistics including total file size and status code counts.

    :param total_size: Total file size.
    :param status_counts: A dictionary containing status code counts.
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")


def parse_log(line, total_size, status_counts):
    """
    Parse a log line and update the total size and status code counts.

    :param line: The log line to parse.
    :param total_size: Total file size.
    :param status_counts: A dictionary containing status code counts.
    :return: A tuple with the updated total size and status counts.
    """
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        file_size = int(parts[-1])
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
    return total_size, status_counts


def main():
    total_size, status_counts = 0, {"200": 0, "301": 0, "400": 0, "401": 0,
                                    "403": 0, "404": 0, "405": 0, "500": 0}
    line_number = 0

    try:
        for line in sys.stdin:
            line_number += 1
            total_size, status_counts = parse_log(line, total_size,
                                                  status_counts)

            if line_number % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
