class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has = dict()
        for word in strs:
            newwd = list(word)
            newwd.sort()
            newwd = ''.join(newwd)
            if newwd in has:
                has[newwd].append(word)
            else:
                has[newwd] = [word]
        return has.values()