class Solution:
    def reverse(self, x: int) -> int:
         #-2,147,483,648 to +2,147,483,647.
        x=str(x)
        negativeFlag = False
        if x.startswith('-'):
            negativeFlag = True
            match = '2147483648'
        else:
            match = '2147483647'
        x= x.strip('-')[::-1]
        if len(x) > len(match):
            return 0
        elif len(x) < len(match):
            if negativeFlag:
                return  int(x) - (int(x)+int(x))
            else:
                return int(x)
        else:
            for _index in range(len(x)):
                if int(x[_index]) < int(match[_index]):
                    if negativeFlag:
                        return  int(x) - (int(x)+int(x))
                    else:
                        return int(x)
                elif int(x[_index]) == int(match[_index]):
                    pass
                else:
                    return 0
            return 0