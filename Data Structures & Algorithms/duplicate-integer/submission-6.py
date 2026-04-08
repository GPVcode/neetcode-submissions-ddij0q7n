class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) < 2:
                return False

        seen = set()

        for val in nums:
                print(seen)
                if val in seen:
                        return True
                seen.add(val)
                print(val)


        return False

        # time: O(N)
        # space: O(N)