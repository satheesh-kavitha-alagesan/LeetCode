# class Trie:
#     def __init__(self):
#         self.store={}
    
#     def insert(self, word):
#         di = self.store
#         for char in word:
#             di[char] = {}
#             di = di[char]
#         di['#'] = None
#         return self.store
    
#     def search(self, listOfWords, st):
#         newst = None
#         def rec(stbac, word):
#             print(f'{stbac = }')
#             print(f'{word = }')
#             for char in word:
#                 if char in stbac:
#                     stbac = stbac[char]
#                 else:
#                     return False
#             print(f'{stbac = }')
#             newst = stbac
#             return True

#         for word in listOfWords:
#             newst = None
#             if rec(stbac = st, word = word):
#                 if newst != None:
#                     if '#' in newst:
#                         return True
#                 self.search(listOfWords, newst)
#         return False

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         tr = Trie()
#         lad = tr.insert(s)
#         print(lad)
#         return tr.search(wordDict, lad)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def construct(current,wordDict, memo={}):
            if current in memo:
                return memo[current]

            if not current:
                return True

            for word in wordDict:
                if current.startswith(word):
                    new_current = current[len(word):]
                    if construct(new_current,wordDict,memo):
                        memo[current] = True
                        return True

            memo[current] = False
            return False

        return construct(s,wordDict)