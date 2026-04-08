class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # edge case only 1 in list
        if len(nums) < 2:
            return nums
        # need a list for storage
        # dictionary to track count

        dictionary = {}

        # loop
            # not in dictionary set key and count
            # in dictionary add to count
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else: 
                dictionary[i] += 1

        return sorted(dictionary, key=dictionary.get, reverse=True)[:k]
        
