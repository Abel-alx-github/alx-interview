#!/usr/bin/python3
""" a module contains a script that parse input from stdin"""

import sys
import re


if __name__ == '__main__':
    pattern_str = (
        r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s-\s\[\d{4}-\d{2}-\d{2}\s"
        r"\d{2}:\d{2}:\d{2}\.\d+\]\s\"GET /projects/260 HTTP/1.1\"\s\d{3}\s\d+"
    )

    dic = {}
    list_status = [500, 405, 404, 403, 401, 400, 301, 200]
    file_size = 0
    count = 0

    def print_metric(dic, file_size):
        print("File size:", file_size)
        for k in list_status:
            if k in dic.keys():
                print("{}: {}".format(k, dic[k]))

    try:
        for line in sys.stdin:
            count += 1
            if not line:
                break
            found = re.search(pattern_str, line)
            if found:
                size = int(list(found.string.split())[-1])
                status = int(list(found.string.split())[-2])
                if status in list_status:
                    if status in dic.keys():
                        dic[status] += 1
                        file_size += size
                    else:
                        dic[status] = 1
                        file_size += size
            if count % 10 == 0:
                print_metric(dic, file_size)
    except KeyboardInterrupt:
        raise
    finally:
        print_metric(dic, file_size)
