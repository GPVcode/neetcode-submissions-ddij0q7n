class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        the_diction = {}

        for i in s:
            if i not in the_diction:
                the_diction[i] = 1
            else:
                the_diction[i] += 1
        print(the_diction)

        for i in t:
            if i not in the_diction:
                return False
            elif the_diction[i] == 0:
                return False
            else:
                the_diction[i] -= 1

        return True