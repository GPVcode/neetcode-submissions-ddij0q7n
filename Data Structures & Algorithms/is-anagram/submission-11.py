class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length is not equal
        if len(s) != len(t):
            return False
        s_map = {}
        # create map out of s with count as value
        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i] += 1

        print(s_map)
        # loop
        for i in t:
            if i not in s_map:
                return False
            elif s_map[i] == 0:
                return False
            else:
                s_map[i] -= 1
                
        return True

