#!/usr/bin/python3
""" validata utf-8 data set"""


def validUTF8(data):
    ones = 0
    for num in data:
        if ones == 0:
            if num >> 5 == 0b110:
                ones = 1
            elif num >> 4 == 0b1110:
                ones = 2
            elif num >> 3 == 0b11110:
                ones = 3
            elif num >> 7:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            ones -= 1
    return ones == 0
