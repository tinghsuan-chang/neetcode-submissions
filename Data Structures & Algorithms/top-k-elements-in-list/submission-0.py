class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)] # [[], [nums that appear once], [nums that appear twice],...]

        for num, count in num_count.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Time: O(n)
# Space: O(n)

        

        
