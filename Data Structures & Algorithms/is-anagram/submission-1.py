class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r = s.sorted()
        y = t.sorted()
        if r == y:
            return True
        
        else:
            return False

        