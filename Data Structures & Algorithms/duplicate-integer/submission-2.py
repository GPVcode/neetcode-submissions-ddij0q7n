class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) < 2:
                return False

        dictionary = {}

        for i, val in enumerate(nums):
                if val not in dictionary:
                        dictionary[val] = 1
                else:
                        dictionary[val] += 1

        for i, val in enumerate(nums):
                if dictionary[val] > 1:
                        return True

        return False

        # time: O(N)
        # space: O(N)