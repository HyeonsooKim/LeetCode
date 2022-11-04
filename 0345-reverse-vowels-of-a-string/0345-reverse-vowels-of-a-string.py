class Solution:
    def reverseVowels(self, s: str, vwls = set(list("aeiouAEIOU"))) -> str:
        
        l, r, s = 0, len(s) - 1, list(s)
        while l < r:                           
            while l < r and s[l] not in vwls: l += 1     # [1] move pointers until
            while l < r and s[r] not in vwls: r -= 1     #     two vowels are found 
            s[l], s[r] = s[r], s[l]                      # [2] swap vowels and move
            l, r = l + 1, r - 1                          #     pointers further
        return "".join(s)