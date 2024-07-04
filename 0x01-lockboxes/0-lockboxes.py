#!/usr/bin/python3

""" You have n number of locked boxes in front of you.
  Each box is numbered sequentially from 0 to n - 1
  and each box may contain keys to the other boxes.

  Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """ boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """

    if not boxes:
        return

    opened_boxes = set()

    queue = [0]

    while queue:
        current = queue.pop(0)

        if current not in opened_boxes:
            opened_boxes.add(current)

            for key in boxes[current]:
                if key not in opened_boxes and key < len(boxes):
                    queue.append(key)

    return len(opened_boxes) == len(boxes)
