class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            one = cost[i] + cost[i+1]
            two = cost[i] + cost[i+2]
            cost[i] = min(one, two)
        
        return min(cost[0], cost[1])

            