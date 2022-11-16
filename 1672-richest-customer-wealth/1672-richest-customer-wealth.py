class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ls = [sum(i) for i in accounts]
        return max(ls)