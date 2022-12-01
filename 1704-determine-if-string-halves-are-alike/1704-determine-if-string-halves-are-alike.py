class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        cnt_a = 0
        cnt_b = 0
        for i, j in zip(a, b):
            if i in vowels:
                cnt_a += 1
            if j in vowels:
                cnt_b += 1
        
        return cnt_a == cnt_b