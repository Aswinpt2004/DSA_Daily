class Solution:
    def minimumCost(self, nums):
        first_cost = nums[0]

        rest = nums[1:]

        rest.sort()

        return first_cost + rest[0] + rest[1]
