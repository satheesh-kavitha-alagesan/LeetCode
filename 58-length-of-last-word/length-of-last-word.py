class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for ind, char in enumerate(s.rstrip(' ')[::-1]):
            if char == ' ':
                return ind
        return ind+1