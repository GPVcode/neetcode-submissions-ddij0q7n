class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case not equal length
        if len(s) != len(t):
            return False
        # dictionary with count
        my_dict = {}
        for i in s:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for i in t:
            if i not in my_dict:
                return False
            elif my_dict[i] == 0:
                return False
            else:
                my_dict[i] -= 1

        return True