class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counts = {}   
        
        if len(s) != len(t):
            return False

        for char in s:
            counts[char] = counts.get(char,0) + 1
        
        for char in t:
            counts[char] = counts.get(char,0) - 1

        for val in counts.values():
            if val != 0:
                return False
        
        return True