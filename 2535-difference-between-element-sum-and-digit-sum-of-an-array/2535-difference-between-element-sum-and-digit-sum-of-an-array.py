class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es = 0
        ds = 0
        for i in nums:
            es += i
            if i > 9:
                ls = list(map(int, list(str(i))))
                ds += sum(ls)
            else:
                ds += i
                
        return abs(es-ds)