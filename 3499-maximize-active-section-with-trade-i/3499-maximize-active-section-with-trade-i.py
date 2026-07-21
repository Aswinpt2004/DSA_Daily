from itertools import groupby

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        ans = ones

        t = "1" + s + "1"
        runs = [(ch, len(list(g))) for ch, g in groupby(t)]

        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1':
                left = runs[i - 1][1]
                right = runs[i + 1][1]
                ans = max(ans, ones + left + right)

        return ans