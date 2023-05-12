#!/usr/bin/python3
"""Log parsing Module
"""


if __name__ == "__main__":
    status_appearance = {
        '200': 0, '301': 0, '400': 0,
        '401': 0, '403': 0, '404': 0,
        '405': 0, '500': 0
    }
    file_size = 0

    def print_statistics() -> None:
        """Prints the accumulated statistics of the HTTP request log.

        Args:
            total_file_size (int): _description_
            status_codes_stats (Dict[int, int]): _description_
        """
        print('File size: {:d}'.format(file_size), flush=True)
        for key, value in sorted(
                status_appearance.items(),
                key=lambda x: x[1], reverse=True):
            if value > 0:
                print(*("{}: {}".format(key, value)), sep='', flush=True)

    try:
        while True:

            temp = input().split(sep=" ")
            if len(temp) > 6:
                try:
                    file_size += int(temp[-1])
                    status_appearance[temp[-2]] += 1
                except KeyError:
                    continue

                if sum(status_appearance.values()) % 10 == 0:
                    print_statistics()

    except (KeyboardInterrupt, EOFError):
        print_statistics()
