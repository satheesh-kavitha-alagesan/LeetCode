class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rem = 0
        alen = len(a)
        blen = len(b)
        if alen > blen:
            b = ''.join(['0']*(alen - blen))+b
        if blen > alen:
            a = ''.join(['0']*(blen - alen))+a
        ret = ''
        for ind in range(len(a)-1, -1, -1):
            print(ind)
            if a[ind] == '0' and b[ind] == '0':
                ret = str(rem) + ret
                rem = 0
            elif a[ind] == '1' and b[ind] == '1':
                ret = str(rem) + ret
                rem = 1
            else:
                if rem == 1:
                    ret = '0' + ret
                    rem = 1
                else:
                    ret = '1' + ret
                    rem = 0
        if rem == 1:
            return '1' + ret
        else:
            return ret