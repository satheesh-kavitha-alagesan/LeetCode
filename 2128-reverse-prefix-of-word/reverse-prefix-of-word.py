class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        rev = ''
        while word:
            if word[0] == ch:
                rev = ch + rev
                word = word[1::]
                return rev+word
            rev = word[0] + rev
            word = word[1::]
        return rev[::-1]