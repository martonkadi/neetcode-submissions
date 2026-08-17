class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minValue = prices[0]

        for i in range(len(prices)):
            # minValue = min(prices[0:i+1])
            if prices[i] < minValue:
                minValue = prices[i]
            if prices[i] - minValue > profit:
                profit = prices[i] - minValue
        
        return profit