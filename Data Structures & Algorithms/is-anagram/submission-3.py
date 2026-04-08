class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        # use dictionary to keep count
        dictionary = {}

        # create a dictionary with string 1 with 1 as the value
        for i, val in enumerate(list(s)): 
            if val in dictionary:
                print(val)
                dictionary[val] += 1
            else:
                print("else", val)
                dictionary[val] = 1
            
        print(dictionary.keys(), dictionary.values())
        

        for i, val in enumerate(list(t)):
            if val not in dictionary:
                return False
            elif dictionary[val] == 0:
                return False
            else:
                dictionary[val] -= 1
            
        print(dictionary.keys(), dictionary.values())

        
        return True

