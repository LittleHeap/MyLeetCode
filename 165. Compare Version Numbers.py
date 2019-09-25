class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        version1 = version1.split('.')
        version2 = version2.split('.')

        while version1 and version2:
            c1 = int(version1.pop(0))
            c2 = int(version2.pop(0))
            if c1 > c2:
                return 1
            elif c1 < c2:
                return -1

        while version1:
            c1 = int(version1.pop(0))
            if c1 != 0:
                return 1

        while version2:
            c2 = int(version2.pop(0))
            if c2 != 0:
                return -1

        return 0
