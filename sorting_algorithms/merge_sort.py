"""
Merge Sort.
TODO: Add type hints for the functions.
TODO: Add test cases.
TODO: Add merge sort for linked list.
"""


def merge_sort(array):
    """
    Sorts a list in ascending order using divide and conquer.
    Time complexity: O(n log n)
    Space complexity: O(n)
    :param array: List to be sorted.
    :return: Sorted list.
    """
    if len(array) <= 1:  # Base case where the array is a single char.
        return array

    mid = len(array) // 2  # Rounds to the bottom value.
    left = merge_sort(array[:mid])  # Without the middle value.
    right = merge_sort(array[mid:])  # With the middle value.

    # the first merge will be the left most, lowest part of the tree.
    return merge(left, right)


def merge(left, right):
    """
    Merging bein done via the 2 pointer technique
    Time Complexity: O(n)
    Space Complexity: O(1)
    :param left:
    :param right:
    :return:
    """
    merged = []  # Sorted array to be returned.
    i, j = 0, 0  # Pointers for left and right array respectively.

    while i < len(left) and j < len(right):  # Till one of the arrays is empty.
        if left[i] <= right[j]:  # Find smallest and append to the merged array, increment pointer.
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # After one of the arrays is empty, we dump the remaining into merged.
    # The dumping includes the ith and jth value (because it got incremented).
    # Empty arrays do not append anything to the merged array.
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
