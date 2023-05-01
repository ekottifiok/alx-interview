#!/usr/bin/python3
"""
A script for parsing HTTP request logs.
and it's an interview
"""
from re import fullmatch
from typing import Dict
from copy import deepcopy

def update_metrics(
        line: str,
        total_file_size: int,
        status_codes_stats: Dict[int, int]) -> int:
    """Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): _description_
        status_codes_stats (Dict[str, int]): _description_

    Returns:
        int: The new total file size.
    """

    def extract_input() -> Dict[str, int]:
        """
        Extracts sections of a line of an HTTP request log.

        Args:
            input_line (str): the line inputted by the user

        Returns:
            Dict[str, None]: the data extracted
        """

        r = fullmatch(
            '{}\\-{}{}{}{}\\s*'.format(
                r'\s*(?P<ip>\S+)\s*',
                r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
                r'\s*"(?P<request>[^"]*)"\s*',
                r'\s*(?P<status_code>\S+)',
                r'\s*(?P<file_size>\d+)'
            ),
            line)
        return {
            'status_code': int(r.group('status_code') if r is not None else 0),
            'file_size': int(r.group('file_size')) if r is not None else 0
        }

    line = extract_input()
    status_code = line.get('status_code', 0)
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line['file_size']


if __name__ == '__main__':
    """Starts the log parser. makes the everything to run
    Its the main function in the module
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0,
    }

    def print_statistics(
            total_file_size: int,
            status_codes_stats: Dict[int, int]) -> None:
        """Prints the accumulated statistics of the HTTP request log.

        Args:
            total_file_size (int): _description_
            status_codes_stats (Dict[int, int]): _description_
        """
        print('File size: {:d}'.format(total_file_size), flush=True)
        for status_code in sorted(status_codes_stats.keys()):
            num = status_codes_stats.get(status_code, 0)
            if num > 0:
                print('{:d}: {:d}'.format(status_code, num), flush=True)

    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
                
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)
