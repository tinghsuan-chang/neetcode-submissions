import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      profit = 0
      buy = math.inf
      
      for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif (prices[i] > buy) and (prices[i] - buy > profit):
            profit = prices[i] - buy
      
      return profit
    