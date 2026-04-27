class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Edge case:
        if len(nums) < 2: 
            return False
        map = {}
        # {3: 0}

        for i, value in enumerate(nums):
            complement = target - value
            # if complement is not in map then add this value in map
            if complement not in map:
                map[value] = i
                print("print: ", min(map[value], 65))
            # otherwise return
            else:
                return [min(i, map[complement]), max(i, map[complement])]
            print(map)

        return False
