# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         ret = set()
#         temp = ''
#         def rec(ind, temp):
#             print(f'{temp = }')
#             if (temp != '') and (temp == temp[::-1]):
#                 ret.add(temp)
#             if ind >= len(s):
#                 return
#             temp = temp + s[ind]
#             rec(ind+1, temp)
#             temp = temp[0:-1]

#         rec(0, temp)
#         print(ret)
#         return ret

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[n] = [[]]
        for begin in range(n - 1, -1, -1):
            for end in range(begin + 1, n + 1):
                candidate = s[begin:end]
                if candidate == candidate[::-1]:
                     for each in dp[end]:
                         new_each = [candidate]
                         new_each.extend(each)
                         dp[begin].append(new_each)
        return dp[0]  
