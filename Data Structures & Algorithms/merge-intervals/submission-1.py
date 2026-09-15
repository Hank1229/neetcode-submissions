class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            res = []
            intervals.sort()
            res.append(intervals[0])

            for start, end in intervals:
                if start and end < res[-1][1]:
                    continue

                elif res[-1][1] <= end and res[-1][1] >= start:
                     res[-1][1] = max(res[-1][1], end)
                else:
                    res.append([start,end])
            return res



[1,4]
       