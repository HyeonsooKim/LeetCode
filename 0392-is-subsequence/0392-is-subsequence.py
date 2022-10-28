class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        
        
        pos = -1
        answer = []

        for i in s:
            ls = t[pos+1:]
            if i in ls:
                idx = ls.index(i) + 1
                answer.append(pos+idx)
                pos = pos+idx
            else:
                return False
        return sorted(answer) == answer
        
        