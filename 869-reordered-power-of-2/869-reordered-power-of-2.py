from collections import Counter
from itertools import permutations
import math
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ls = [int(''.join(i)) for i in list(permutations(str(n), len(str(n)))) if i[0] != '0']
        poweroftwo = []
        # 2의 거듭제곱으로 나타낼 수 있는 수의 리스트 (10e9이내)
        for i in range(34):
            poweroftwo.append(1<<i)

        for i in ls:
            if i in poweroftwo:
                return True
        else:
            return False


# 베스트 풀이
# POWERS = {''.join(sorted(str(1<<n))) for n in range(31)}
# def reorderedPowerOf2(self, n: int) -> bool:
#     return ''.join(sorted(str(n))) in POWERS