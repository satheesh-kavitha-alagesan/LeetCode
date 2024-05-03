class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [ int(v) for v in version1.split('.') ]
        version2 = [ int(v) for v in version2.split('.') ]

        if len(version2) > len(version1):
            version1.extend([0]*(len(version2) - len(version1)))
        elif len(version1) > len(version2):
            version2.extend([0]*(len(version1) - len(version2)))

        for v1, v2 in zip(version1, version2):
            if v1>v2:
                return 1
            elif v2>v1:
                return -1
        return 0