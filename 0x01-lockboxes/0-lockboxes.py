#!/usr/bin/python3

'''An implementation of the lockboxes problem is provided in this module
'''

def canUnlockAll(boxes):
    """A function to determine if all boxes can be opened. boxes is a list of lists,
    where each list represents a box. Return True if all boxes can be openend,
    False otherwise
    """

    all_keys = set([*range(1, len(boxes))])
    found_keys = set()

    for i in range(len(boxes)):
        if found_keys >= all_keys:
            return True
        if i > 0 and i not in found_keys:
            return False
        for key in boxes[i]:
            found_keys.update({i, key})
            if found_keys >= all_keys:
                return True
            if key >= len(boxes):
                continue
            for item in boxes[key]:
                found_keys.add(item)
                if found_keys >= all_keys:
                    return True
                
