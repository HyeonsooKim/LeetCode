class Solution:
    def minimumSum(self, num: int) -> int:
        n=[num//1000,(num//100)%10,(num//10)%10,num%10]
        n.sort()
        return (n[0]*10+n[3])+(n[1]*10+n[2])