"""
Two pointers explanation: https://www.reddit.com/r/leetcode/comments/18g9383/twopointer_technique_an_indepth_guide_concepts/

Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        Plan:
        hashmap + sorta kinda two pointers
        Using the compliment = target - value, where,
            if a pair exists, atleast 2 elements in the list will have their compliments in the hashmap.
        Time complexity: O(n)
        Space complexity: O(n)
        """

        hashmap = {}
        for index in range(len(nums)):
            compliment = target - nums[index]
            if compliment in hashmap:
                return [hashmap[compliment], index]
            else:
                hashmap[
                    nums[index]] = index  # the value of the index is stored as key to retrieve the index in the future
        return []  # no pair found, return empty array
