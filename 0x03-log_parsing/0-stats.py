#!/usr/bin/python3
""" a module contains a script that parse input from stdin"""

if __name__ == '__main__':
    import sys
    file_size = 0
    count = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    dic_stats = {k: 0 for k in status_codes}

    def print_metric(dic_stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for k, v in sorted(dic_stats.items()):
            if v:
                print("{}: {}".format(k, v))
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                stat_code = data[-2]
                if stat_code in dic_stats:
                    dic_stats[stat_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_metric(dic_stats, file_size)
        print_metric(dic_stats, file_size)
    except KeyboardInterrupt:
        print_metric(dic_stats, file_size)
        raise
