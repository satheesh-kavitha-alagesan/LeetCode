class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ind = len(digits) - 1
        while digits[ind] == 9:
            digits[ind] = 0
            ind = ind -1
            if ind ==-1:
                break
        if ind == -1:
            return [1] + digits
        else:
            digits[ind] += 1
            return digits