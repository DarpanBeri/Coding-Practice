"""
153. Find Minimum in Rotated Sorted Array
First one that I did!! took a day tho lol : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""

# Challenge is to make the solution log n, which means halving the array in cosideration.
# Which means using middle_index_pointer to make decisions.

# Straight forward solution:
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # O(n) implementation -> linear search
        # O(log n) implementation -> binary search

        """
        Plan: 
        1. Rotation means that from a middle index perspective, one half of the array is sorted.
        2. The numbers have a relation to each other where they ascend to the right until the pivot.
        3. Log relation is cascadingly decrease the numbers under consideration by half.
            a. Take the first, mid and last number.
            b. if nums[mid] > nums [right], make left_index_pointer -> mid+1
            c. elif nums[mid] < nums [right], that means that mid-right is sorted, no pivot.
                c.1 In this case, we consider left to mid in the next iteration.
                c.2 so right_index_pointer -> mid.
            c. Repeat till left_index_pointer < right_index_pointer then return nums[left]
        """
        # straight forward solution
        left_index_pointer = 0
        right_index_pointer = len(nums) - 1

        while left_index_pointer < right_index_pointer:
            middle_index_pointer = (left_index_pointer + right_index_pointer) // 2

            if nums[middle_index_pointer] > nums[right_index_pointer]:
                left_index_pointer = middle_index_pointer + 1  # Shifting the array in consideration to right of mid.
            else:
                # Mid to right is already sorted.
                # Shift the array to the left.
                right_index_pointer = middle_index_pointer

        return nums[left_index_pointer]

# Recursive solution that makes sense to me (bad memory complexity)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # O(n) implementation -> linear search
        # O(log n) implementation -> binary search

        """
        Plan: 
        1. Rotation means that from a middle index perspective, one half of the array is sorted.
        2. The numbers have a relation to each other where they ascend to the right until the pivot.
        3. Log relation is cascadingly decrease the numbers under consideration by half.
            a. Take the first, mid and last number.
            b. if nums[mid] > nums [right], make left_index_pointer -> mid+1
            c. elif nums[mid] < nums [right], that means that mid-right is sorted, no pivot.
                c.1 In this case, we consider left to mid in the next iteration.
                c.2 so right_index_pointer -> mid.
            c. Repeat till left_index_pointer < right_index_pointer then return nums[left]
        """

        def recursive_sol(array):
            first_index = 0
            last_index = len(array) - 1

            if first_index == last_index:  # Base case, if only one elem in array, return elem.
                return array[first_index]

            middle_index = last_index // 2  # Rounds to floor.

            if array[middle_index] > array[last_index]:
                # Pivot is to the right of middle_index
                return recursive_sol(array[middle_index + 1:])
            else:
                # Pivot is to the left of the middle index, inclusive of middle index
                return recursive_sol(array[:middle_index + 1])

        return recursive_sol(nums)
