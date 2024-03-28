#Solution 1 Major pass Timeout failure
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         curind = 0
#         iteration = 0
#         le = len(gas)
#         val = 0
#         while gas and cost:
#             iteration +=1
#             g = gas.pop(0)
#             c = cost.pop(0)
#             gas.append(g)
#             cost.append(c)
#             val +=g
#             val -= c
#             if (iteration > le+1) and (val < 0):
#                 return -1
#             if val >=0:
#                 curind +=1
#                 if curind == le:
#                     return iteration - le
#             else:
#                 val = 0
#                 curind = 0


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1   
        tank = idx = 0                          
        for i in range(len(gas)):            
            tank+= gas[i]-cost[i]             
            if tank < 0: tank, idx = 0, i+1  
        return idx                           
                                             
                                             