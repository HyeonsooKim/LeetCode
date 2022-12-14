class Solution:
    def sumBase(self, n: int, k: int) -> int:
        base = ''
        
        while n > 0:
            n, mod = divmod(n, k)
            base += str(mod)
        
        base = base[::-1]
        ans = 0
        for i in base:
            ans += int(i)
        
        return ans