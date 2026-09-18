class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            res = []
            intervals.sort()
            res.append(intervals[0])

            for start, end in intervals:
                if res[-1][1] >= start:
                   res[-1][1] = max(res[-1][1], end)
                else:
                    res.append([start, end])
            return res
                        



       