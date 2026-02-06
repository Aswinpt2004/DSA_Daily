class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)

        right = 0
        best = 0

        for left in range(N):
            while right < N and nums[right] <= nums[left] * k:
                right += 1

            best = max(best, right - left)

        return N - best
