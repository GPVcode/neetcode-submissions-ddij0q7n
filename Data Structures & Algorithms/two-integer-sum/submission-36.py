class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}

        for i, value in enumerate(nums):
            complement = target - value
            if complement not in my_dict:
                my_dict[value] = i
            else:
                return [min(my_dict[complement], i), max(my_dict[complement], i)]