class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-s for s in stones]
        heapq.heapify(min_heap)

        while len(min_heap) >= 2:
            s1 = heapq.heappop(min_heap)
            s2 = heapq.heappop(min_heap)
            if s1 != s2:
                heapq.heappush(min_heap, s1 - s2)
            
        
        if min_heap:
            return -min_heap[0]
        else:
            return 0