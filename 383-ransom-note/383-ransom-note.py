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

# 좋은 솔루션
# Counter 함수는 문자열에서 문자열이 나오는 횟수를 Dictionary 형태로 만들어주는 함수
# from itertools import Counter
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         magazine = Counter(magazine)
#         ransomNote = Counter(ransomNote)
#         return all(magazine[c] >= ransomNote[c] for c in ransomNote)