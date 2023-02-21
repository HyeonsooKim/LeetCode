from collections import Counter, OrderedDict
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x = Counter(nums)
        y = list(OrderedDict(x.most_common()))
        return y[-1]
        