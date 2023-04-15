#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
from re import fullmatch
from typing import Dict, List


def extract_input(input_line: str) -> Dict[str, int]:
    """
    Extracts sections of a line of an HTTP request log.

    Args:
        input_line (str): the line inputted by the user

    Returns:
        Dict[str, None]: the data extracted
    """
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': '0',
        'file_size': 0,
    }

    resp_match = fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(
    total_file_size: int,
    status_codes_stats: Dict[str, int]) -> None:
    """Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (_type_): _description_
        status_codes_stats (_type_): _description_
    """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(
    line: str,
    total_file_size: int,
    status_codes_stats: Dict[str, int]) -> int:
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats['status_code'] += 1
    return total_file_size + line_info['file_size']


def run() -> None:
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
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


if __name__ == '__main__':
    run()
