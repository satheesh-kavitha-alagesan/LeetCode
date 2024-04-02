class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(' ')
        return ' '.join([i for i in s.split(' ')[::-1] if i!= ''])