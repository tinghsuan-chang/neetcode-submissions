class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) # Time: O(n)
        while len(self.minHeap) > k: # Time: O((n-k)logn) or O(nlogk) when n>>k
            heapq.heappop(self.minHeap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # Time: O(logk)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # Time: O(logk)
        return self.minHeap[0]
