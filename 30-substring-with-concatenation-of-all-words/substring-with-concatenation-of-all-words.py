# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         l = len(words)

#         class StringCheck:
#             def __init__(self, wds):
#                 self.wds = wds
            
#             def checkewith(self, st):
#                 self.stripword = ''
#                 for w in self.wds:
#                     if st.endswith(w):
#                         self.stripword = w
#                         return True
#                 return False

#         ch=StringCheck(wds = words)
#         ret = []
#         while s:
#             count = 0
#             while ch.checkewith(s) and count < l:
#                 count+=1
#                 s.rstrip(ch.stripword)
#                 if count == l:
#                     ret.append(len(s)-1)
#                     count = 0
#             s = s[0:-1]
#         print(ret)
#         return ret

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordc = {}
        ret = []
        for wd in words:
            if wd in wordc:
                wordc[wd] = wordc[wd] + 1
            else:
                wordc[wd] = 1
            
        lengofst = len(s)
        lowd = len(words[0])
        reqlen = lowd*len(words)
        for ind in range(lengofst +1 - reqlen):
            stf = s[ind::]
            curwd = stf[0:lowd]
            tempword = defaultdict(int)
            flag = True
            for _ in range(len(words)):
                if wordc.get(curwd, None):
                    if (tempword[curwd] + 1) <= wordc[curwd]:
                        tempword[curwd] = tempword[curwd] + 1
                        stf = stf[lowd::]
                        curwd = stf[0:lowd]
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                ret.append(ind)
        return ret