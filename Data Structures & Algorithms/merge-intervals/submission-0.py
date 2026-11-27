class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals in ascending order based on start value
        intervals.sort(key = lambda x: x[0])
        
        if len(intervals) == 1:
            return intervals

        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[i - 1][1]:
                start = intervals[i - 1][0]
                end = max(intervals[i - 1][1], intervals[i][1])
                intervals[i] = [start, end]
            else:
                res.append(intervals[i - 1])
            if i == len(intervals) - 1:
                res.append(intervals[i])
        
        return res
            

            