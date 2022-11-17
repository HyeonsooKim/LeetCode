# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        end = n
        while True:
            mid = (first+end) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                first = mid+1
            else:
                end = mid
            if guess(first) == 0:
                return first
            if guess(end) == 0:
                return end
        
                
        