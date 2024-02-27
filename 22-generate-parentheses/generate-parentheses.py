class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res = []
        # def back(st, opencount, closecount):
        #     if len(st) == 2*n:
        #         res.append(st)
        #         return
        #     if opencount < n:
        #         back(st+'(', opencount+1, closecount)
        #     if closecount < opencount:
        #         back(st + ')', opencount, closecount+1)
        # back('', 0, 0)
        # return res

        res = []
        opencount = 0
        closecount = 0
        track = [(opencount, closecount, '')]
        while track:
            opencount, closecount, st = track.pop()
            if len(st) == 2*n:
                res.append(st)
            if opencount < n:
                track.append((opencount+1, closecount, st + '('))
            if closecount < opencount:
                track.append((opencount, closecount+1, st + ')'))
        return res