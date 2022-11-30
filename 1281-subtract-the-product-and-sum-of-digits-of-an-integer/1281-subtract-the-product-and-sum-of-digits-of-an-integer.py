class Solution:
    def subtractProductAndSum(self, n: int) -> int:
            prod = 1        # n =234
            sums = 0
            while n != 0:       #           1st loop     2nd loop    3rd loop 
                last = n % 10   # last =    4            3           2
                prod *= last    # prod =    1*4 = 4      4*3 = 12    12*2 = 24
                sums += last    # sums =    0+4 = 4      4+3 = 7     7+2 = 9
                n =n//10        # n    =    23           2           0
            return prod - sums  # 24 - 9 = 15