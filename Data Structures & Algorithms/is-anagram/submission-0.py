class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.sorted()
        t.sorted()
        if s == t:
            return True
        else:
            return False
        