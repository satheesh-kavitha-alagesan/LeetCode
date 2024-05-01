class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        for i in range(0, len(word)):
            if word[i] == ch:
                index = i
                break
        if index != 0:
            return word[0:index+1][::-1] + word[index+1::]
        return word