class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        temp = [[i] for i in candidates]
        secondOrder = []
        while temp:
            curli = temp.pop()
            s = sum(curli)
            if s == target:
                curli.sort()
                if curli not in ret:
                    ret.append(curli)
            elif s > target:
                if len(temp) == 0:
                    temp = secondOrder
                continue 
            else:
                for ca in candidates:
                    secondOrder.append(curli+[ca])
            if len(temp) == 0:
                temp = secondOrder
        return ret