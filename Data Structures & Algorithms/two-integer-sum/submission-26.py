class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}
        for i, value in enumerate(nums):
            complement = target - value
            if complement not in my_dict.values():
                my_dict[i] = value
            else:
                return [min(nums.index(complement), i), max(nums.index(complement), i)]