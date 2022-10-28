from collections import Counter, defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)): return False
        d = defaultdict()
        new_s = ''
        for i, v in enumerate(s):
            if v not in d.keys():
                d[v] = t[i]
                new_s += t[i]
            else:
                new_s += d[v]

        return new_s == t