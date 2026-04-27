class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Edge case:
        if len(nums) < 2: 
            return False
        seen = {}
        # {3: 0}

        for i, value in enumerate(nums):
            complement = target - value
            # if complement is not in map then add this value in map
            if complement not in seen:
                seen[value] = i
            # otherwise return
            else:
                return [min(i, seen[complement]), max(i, seen[complement])]

        return False
