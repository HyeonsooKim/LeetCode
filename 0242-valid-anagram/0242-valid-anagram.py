class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0] * 30
        l2 = [0] * 30
        if len(s) != len(t): return False
        for i, j in zip(s, t):
            l1[ord(i)-97] += 1
            l2[ord(j)-97] += 1
            
        if l1 == l2:
            return True
        else:
            return False