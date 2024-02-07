class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            numBack = x
            tempNum = 0
            while numBack > 0:
                tempNum = tempNum*10 + numBack % 10
                numBack = numBack // 10
            if tempNum == x:
                return True
            return False