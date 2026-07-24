from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        mx = max(nums) << 1

        st = [False] * mx
        for a in nums:
            for b in nums:
                st[a ^ b] = True

        seen = [0] * mx
        for ab in range(mx):
            if st[ab]:
                for c in nums:
                    seen[ab ^ c] = 1

        return sum(seen)