# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         mini = None
#         maxi = None
#         profit = 0
#         while prices:
#             pop = prices.pop(0)
#             if (mini == None):
#                 mini = pop
#                 continue
#             if pop <= mini:
#                 mini =pop
#                 continue
#             elif maxi == None:
#                 maxi = pop
#             while prices:
#                 if prices[0] > pop:
#                     maxi = prices.pop(0)
#                 else:
#                     break
#             profit += (maxi - mini)
#             maxi = None
#             mini = None
#         if (mini != None) and (maxi != None):
#             profit += (maxi - mini)
#         return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        days = len(prices)
        for i in range(1, days):
            if buy < prices[i]:
                profit += prices[i] - buy
            buy = prices[i]
        return profit