class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)

        best = 0
        for start in range(N):
            odd =  set()
            even = set()

            for end in range (start , N):
                if nums[end] % 2 == 0:
                    even.add(nums[end])
                else:
                    odd.add(nums[end])

                if len(even) == len(odd):
                    best =  max(best,end - start + 1)
        return best
                 
        