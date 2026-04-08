class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        # dictionary
        nums_dictionary = {}
        # loop
        for i in nums:
            # find outcome
            if i not in nums_dictionary:
                nums_dictionary[i] = 1
            else:
                return True
            

        return False