class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = 10e5
        max_value = 0
        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            elif prices[i] - min_value > max_value:
                max_value = prices[i] - min_value
        return max_value
    