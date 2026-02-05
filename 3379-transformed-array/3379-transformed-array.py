class Solution:
    def constructTransformedArray(self, nums: Lis[int]) -> List[int]:

        N = len(nums)

        ans = []
        for i in range(N):
            ans.append(nums[(i + nums[i]) % N])
        return ans