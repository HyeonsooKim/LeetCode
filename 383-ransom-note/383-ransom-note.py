class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ls = [0] * (ord('z')+1)
        if ransomNote in magazine:
            return True
        else:
            for i in magazine:
                ls[ord(i)] += 1
            for i in ransomNote:
                ls[ord(i)] -= 1
            for i in range(ord('a'), ord('z')+1):
                if ls[i] < 0:
                    return False
            else:
                return True