class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # finding complement

        if len(nums) < 2:
            return False

        my_dict = {}
    
        # put nums in map.
        # target minus i as logic to find truthy existence

        for i, value in enumerate(nums):
            check = target - value
            if check not in my_dict:
                my_dict[value] = i
            else:
                return [min(i, my_dict[check]), max(i, my_dict[check])]

        return False