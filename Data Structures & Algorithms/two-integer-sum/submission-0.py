class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) < 2:
            return False

        dictionary = {}

        for i, value in enumerate(nums):
            complement = target - value
            if complement in dictionary:
                return [dictionary[complement], i]
            else:
                dictionary[value] = i

        return False