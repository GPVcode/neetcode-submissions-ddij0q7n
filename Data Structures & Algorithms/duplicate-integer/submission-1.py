from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) < 2:
                return False

        # create dictionary
        dictionary = {}
        # loop and fill dictionary
        for i, val in enumerate(nums):
                if val not in dictionary:
                        dictionary[val] = 1
                else:
                        dictionary[val] += 1


        # loop through nums
        for i, val in enumerate(nums):
                if dictionary[val] > 1:
                        return True

        return False


        # time: O(N)
        # space: O(N)