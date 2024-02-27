class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # ret = []
        # temp = [[i] for i in candidates]
        # secondOrder = []
        # while temp:
        #     curli = temp.pop()
        #     s = sum(curli)
        #     if s == target:
        #         curli.sort()
        #         if curli not in ret:
        #             ret.append(curli)
        #     elif s > target:
        #         if len(temp) == 0:
        #             temp = secondOrder
        #         continue 
        #     else:
        #         for ca in candidates:
        #             secondOrder.append(curli+[ca])
        #     if len(temp) == 0:
        #         temp = secondOrder
        # return ret

        tempList=[]
        result=[]
        def backtracking(index,target):
            if target==0:
                result.append(tempList.copy())
                return
            if index>=len(candidates) or target<0:
                return
            for i in range(index,len(candidates)):
                if(target-candidates[i]>=0):
                    tempList.append(candidates[i])
                    ## add the same number or 
                    backtracking(i,target-candidates[i])
                    tempList.pop()
                # add a different number
            # backtracking(i+1,target)
            
        backtracking(0,target)
        return result
                

        
        