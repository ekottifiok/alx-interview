#!/usr/bin/python3
"""
0. Log parsing
mandatory
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this
one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all
    previous <file size> (see input format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

        if a status code doesn't appear or is not an integer,
        don't print anything for this status code

        format: <status code>: <number>
        status codes should be printed in ascending order

Warning: In this sample, you will have random value - it's
normal to not have the same output as this one.
"""


def main():
    """the main working of the parsing
    """
    from sys import stdin
    from re import fullmatch

    pattern = '{}\\-{}{}{}{}\\s*'.format(
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )

    try:
        while (True):
            status_appearance = {
                '200': 0, '301': 0, '400': 0,
                '401': 0, '403': 0, '404': 0,
                '405': 0, '500': 0
            }
            file_size = 0
            for _ in range(10):
                temp = stdin.readline()
                if not fullmatch(pattern, temp):
                    continue
                file_size += int(temp.split()[8])
                status_appearance[temp.split()[7]] += 1
            print('File size:', file_size)
            print(*("{}: {}".format(key, value)
                    for key, value in status_appearance.items()), sep='\n')
    except (KeyboardInterrupt, EOFError):
        return


if __name__ == "__main__":
    main()
