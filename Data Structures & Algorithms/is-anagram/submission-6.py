class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return false
        if sorted(s) == sorted(t):
             
            return true
        else:
            return false
            


        