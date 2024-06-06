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
    if not all(isinstance(item, list) for item in boxes):
        return False
    if not all(isinstance(item, int) for box in boxes for item in box):
        return False

    unseen_boxes = list(range(1, len(boxes)))
    queue = boxes[0]

    for key in queue:
        if key in unseen_boxes:
            queue.extend(boxes[key])
            unseen_boxes.remove(key)
            if len(unseen_boxes) == 0:
                return True
        else:
            queue.remove(key)

    if len(unseen_boxes) == 0:
        return True
    return False
