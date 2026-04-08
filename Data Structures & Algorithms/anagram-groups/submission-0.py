from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # dictionary for
        dictionary = {}

        output = []
        # one loop to store value counts in dictionary

        for i in strs:
            print(dictionary)
            sorted_word = sorted(i)
            core_word = "".join(sorted_word)
            if core_word not in dictionary:
                dictionary[core_word] = [i]
                
            else:
                dictionary[core_word].append(i)
        dict_values = list(dictionary.values())

        return dict_values