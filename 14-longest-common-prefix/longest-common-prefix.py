class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # r= min([len(_i) for _i in strs])
        # ret = ''
        # for ind in range(r):
        #     tem = strs[0][ind]
        #     for elem in strs:
        #         if tem != elem[ind]:
        #             return ret
        #     ret += tem
        # return ret
        ret = ''
        for c in zip(*strs):
            if len(set(c)) == 1:
                ret += c[0]
            else:
                return ret
        return ret