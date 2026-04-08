class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) < 2:
                return False

        dictionary = {}

        for val in nums:
                if val not in dictionary:
                        dictionary[val] = 1
                else:
                        return True

        return False

        # time: O(N)
        # space: O(N)