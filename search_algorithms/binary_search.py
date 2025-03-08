from typing import Sequence, Any


def binary_search(array: Sequence, target: Any) -> int:
    """
    Uses binary search to find the index of a value in an array.
    :param array: Sorted array to be searched.
    :param target: Target to be found in array.
    :return: Index of the target if found, else None.
    """
    first = 0
    last = len(array) - 1

    while first <= last:
        mid = (first + last) // 2  # Rounds to floor.

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            first = mid + 1  # Don't need to check mid.
        else:
            last = mid - 1  # Don't need to check mid.
    return None


def recursive_binary_search(array: Sequence, target: Any) -> int:
    """
    Uses recursive binary search to find the index of the target.
    :param array: Sorted array to be searched.
    :param target: Target to be found in array.
    :return: Index of the target if found, else None.
    """
    if len(array) == 0:  # Stopping condition 1
        return None
    else:
        mid = len(array) // 2

    if array[mid] == target:
        return mid  # Stopping condition 2
    elif array[mid] < target:
        return recursive_binary_search(array[mid+1:], target)
    else:
        # Going array[:mid] vs array[:mid-1] because of how
        # string split works.
        # asd[mid:1] = ['e', 'f'], asd[:mid] = ['a', 'b', 'c', 'd']
        return recursive_binary_search(array[:mid], target)
