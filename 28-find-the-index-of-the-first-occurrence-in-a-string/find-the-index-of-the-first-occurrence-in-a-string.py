class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ind = 0
        while haystack:
            if haystack.startswith(needle):
                return ind
            haystack = haystack[1::]
            ind+=1
        return -1