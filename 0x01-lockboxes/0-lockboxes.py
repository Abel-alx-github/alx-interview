#!/usr/bin/python3
"""
    You have n number of locked boxes in front of you.
    each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes.

    Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """return boolean if boxes are unlocked or not """
    if not isinstance(boxes, list):
        return False
    if len(boxes) <= 1:
        return True
    seen_boxes = set([0])
    queue = [0]

    while (queue):
        for key in boxes[queue.pop(0)]:
            if key not in seen_boxes:
                seen_boxes.add(key)
                queue.append(key)
                if len(seen_boxes) == len(boxes):
                    return True
    return False
