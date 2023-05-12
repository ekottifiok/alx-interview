#!/usr/bin/python3
"""Log parsing Module
"""


if __name__ == "__main__":
    status_appearance = {
        '200': 0, '301': 0, '400': 0,
        '401': 0, '403': 0, '404': 0,
        '405': 0, '500': 0
    }
    file_size, iter = 0, 0

    def print_statistics() -> None:
        """Prints the accumulated statistics of the HTTP request log.

        Args:
            total_file_size (int): _description_
            status_codes_stats (Dict[int, int]): _description_
        """
        print('File size: {:d}'.format(file_size), flush=True)
        print(*("{}: {}".format(key, value)
                for key, value in status_appearance.items() if value > 0),
              sep='\n', flush=True
              )

    try:
        while True:

            temp = input().split()

            if len(temp) != 9:
                continue

            file_size += int(temp[8])
            status_appearance[temp[7]] += 1
            iter += 1
            if iter % 10 == 0:
                print_statistics()

                # resets the variables
                file_size, iter = 0, 0
                status_appearance = {k: 0 for k in status_appearance.keys()}

    except (KeyboardInterrupt, EOFError):
        print_statistics()
