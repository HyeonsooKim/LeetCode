class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = int(''.join(list(map(str,num))))
        ans = list(map(int, list(str(n + k))))
        return ans