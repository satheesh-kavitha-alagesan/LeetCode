# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         total = Counter(s)
#         a = total['a']
#         b=0
#         best = len(s)
#         for char in s:
#             best = min(best, b+a)
#             if char == 'a':
#                 a-=1
#             else:
#                 b+=1
#         best = min(best, b+a)
#         return best

class Solution:
    def minimumDeletions(self, s):
        ans, count = 0, 0
        for i in s:
            if i == 'b':
                count += 1
            elif count:
                ans += 1
                count -= 1
        return ans