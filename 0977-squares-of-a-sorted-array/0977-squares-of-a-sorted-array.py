class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ls = list(map(lambda x : x**2, nums))
        return sorted(ls)