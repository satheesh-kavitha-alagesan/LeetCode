
# Solution 1 Working
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         wordc = {}
#         ret = []
#         for wd in words:
#             if wd in wordc:
#                 wordc[wd] = wordc[wd] + 1
#             else:
#                 wordc[wd] = 1
            
#         lowd = len(words[0])
#         for ind in range(len(s) +1 - lowd*len(words)):
#             stf = s[ind::]
#             curwd = stf[0:lowd]
#             tempword = defaultdict(int)
#             flag = True
#             for _ in range(len(words)):
#                 if wordc.get(curwd, None):
#                     if (tempword[curwd] + 1) <= wordc[curwd]:
#                         tempword[curwd] = tempword[curwd] + 1
#                         stf = stf[lowd::]
#                         curwd = stf[0:lowd]
#                     else:
#                         flag = False
#                         break
#                 else:
#                     flag = False
#                     break
#             if flag:
#                 ret.append(ind)
#         return ret

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt = Counter(words)
        m, n = len(s), len(words)
        k = len(words[0])
        ans = []
        for i in range(k):
            cnt1 = Counter()
            l = r = i
            t = 0
            while r + k <= m:
                w = s[r : r + k]
                r += k
                if w not in cnt:
                    l = r
                    cnt1.clear()
                    t = 0
                    continue
                cnt1[w] += 1
                t += 1
                while cnt1[w] > cnt[w]:
                    remove = s[l : l + k]
                    l += k
                    cnt1[remove] -= 1
                    t -= 1
                if t == n:
                    ans.append(l)
        return ans