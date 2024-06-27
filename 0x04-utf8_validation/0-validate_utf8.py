#!/usr/bin/python3
""" utf-8 validation """


def validUTF8(data):
    """
    data: List[int]
    return type: bool
    """
    ones = 0
    for num in data:
        num = num & 0xFF
        if num & 0x80:
            if ones == 0:
                return False
            ones += 1
            if num & 0xC0 == 0xC0:
                if len(data) < 2:
                    return False
                ones = 2
            elif num & 0xE0 == 0xE0:
                if len(data) < 3:
                    return False
                ones = 3
            elif num & 0xF0 == 0xF0:
                if len(data) < 4:
                    return False
                ones = 4
            else:
                return False
        elif ones > 0:
            if not (num & 0x80 and not (num & 0x40)):
                return False
            ones -= 1
        else:
            ones = 0
    return ones == 0
