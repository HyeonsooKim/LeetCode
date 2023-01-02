class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l = len(word)
        fw = ord(word[0])
        cw = 0
        lw = 0
        for i in range(1, l):
            if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                cw += 1
            else:
                lw += 1
        
        if fw < 91 and (cw == l-1 or lw == l-1):
            return True
        elif fw >= 97 and lw == l-1:
            return True
        else:
            return False