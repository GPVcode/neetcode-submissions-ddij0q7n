class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use map
        # check if i is in map
        my_dict = {}

        for i in nums:
            print(my_dict)
            print(i)
            if i not in my_dict:
                my_dict[i] = 1
            else:
                return True

        return False
    