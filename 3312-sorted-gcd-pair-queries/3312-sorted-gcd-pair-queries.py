from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        exact = [0] * (mx + 1)

        # Count pairs whose numbers are divisible by g
        for g in range(mx, 0, -1):
            cnt = 0
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2

            for multiple in range(g * 2, mx + 1, g):
                pairs -= exact[multiple]

            exact[g] = pairs

        prefix = []
        values = []
        s = 0

        for g in range(1, mx + 1):
            if exact[g]:
                s += exact[g]
                prefix.append(s)
                values.append(g)

        return [values[bisect_right(prefix, q)] for q in queries]