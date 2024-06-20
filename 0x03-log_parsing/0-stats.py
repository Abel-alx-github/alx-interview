#!/usr/bin/python3
""" a module contains a script that parse input from stdin"""


if __name__ == '__main__':
    import sys

    dic = {}
    list_status = [200, 301, 400, 401, 403, 404, 405, 500]
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
            data = line.split()
            try:
                status = int(data[-2])
                size = int(data[-1])
                if status in list_status:
                    if status in dic.keys():
                        dic[status] += 1
                        file_size += size
                    else:
                        dic[status] = 1
                        file_size += size
            except BaseException:
                pass
            if count % 10 == 0:
                print_metric(dic, file_size)
        print_metric(dic, file_size)
    except KeyboardInterrupt:
        print_metric(dic, file_size)
        raise
