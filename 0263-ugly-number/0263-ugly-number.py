class Solution:
    def isUgly(self, n: int) -> bool:
        while True:
            nn = n
            if nn % 2 == 0:
                n /= 2
            if nn % 3 == 0:
                n /= 3
            if nn % 5 == 0:
                n /=5
                
            if nn == n:
                break
        if n == 1:
            return True
        else:
            return False