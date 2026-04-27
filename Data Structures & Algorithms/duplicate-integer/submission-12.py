class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  edge
        if len(nums) < 2:
            return False

        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                return True
        
        return False