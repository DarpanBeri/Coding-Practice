from typing import Sequence, Any


def linear_search(array: Sequence[Any], target: Any) -> int:
    """
    Performs a linear search on an array to find the target value.

    :param array: Array to be searched.
    :param target: Target to be found in the array.
    :return: Index of the target if found, else -1.
    """
    # Base code:
    # for index in range(len(array)):
    #     if array[index] == target:
    #         return index
    # return -1

    # Using python's enumerate:
    for array_index, array_element in enumerate(array):
        if array_element == target:
            return array_index
    return -1
