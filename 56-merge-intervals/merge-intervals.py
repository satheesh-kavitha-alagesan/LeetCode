class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        ret = list()
        ret.append(intervals.pop(0))
        while intervals:
            cur = intervals.pop(0)
            if cur[0] <= ret[-1][1] <= cur[1]:
                ret[-1][1] = cur[1]
            elif (cur[0] >= ret[-1][0]) and (cur[1] <= ret[-1][1]):
                continue
            else:
                ret.append(cur)
        return ret