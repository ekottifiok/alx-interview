#!/usr/bin/python3
"""Unlock box module"""


def canUnlockAll(boxes):
    """Used to unlock boxes"""
    arr = [x for x in range(1, len(boxes))]
    found = set()
    for box in boxes:
        if len(box) == 0 and boxes.index(box) != len(boxes) - 1:
            return False
        for item in box:
            if item in arr:
                found.add(item)
                break
    if len(arr) != len(found):
        return False
    return True
