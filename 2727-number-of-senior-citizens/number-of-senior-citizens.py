class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ret = 0
        for one in details:
            if int(one[11:13]) > 60:
                ret+=1
        return ret