class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        for i, j in zip(indices, s):
            d[i] = j
        ans = ''
        for i in range(len(s)):
            ans += d[i]
        return ans