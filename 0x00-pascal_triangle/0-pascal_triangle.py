#!/usr/bin/python3

''' contain function defination '''


def pascal_triangle(n: int):
    """ function returns pascal triangle"""
    if n <= 0:
        return []
    all_lists = [[1]]

    for i in range(n-1):
        pre_row = all_lists[i]
        new_row = [1]

        for j in range(1, len(pre_row)):
            new_row.append(pre_row[j - 1] + pre_row[j])
        new_row.append(1)
        all_lists.append(new_row)
    return all_lists
