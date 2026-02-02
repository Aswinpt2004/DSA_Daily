from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        n = len(nums)
        
        target_count = k - 1
        
        small = SortedList() 
        large = SortedList() 
        current_small_sum = 0
        
        def add(val):
            nonlocal current_small_sum
            small.add(val)
            current_small_sum += val
            if len(small) > target_count:
                largest_in_small = small.pop(-1)
                current_small_sum -= largest_in_small
                large.add(largest_in_small)
                
        def remove(val):
            nonlocal current_small_sum
            if len(large) > 0 and val >= large[0]:
                large.remove(val)
            else:
                small.remove(val)
                current_small_sum -= val
                if len(large) > 0:
                    smallest_in_large = large.pop(0)
                    small.add(smallest_in_large)
                    current_small_sum += smallest_in_large

        for i in range(1, dist + 2):
            add(nums[i])
            
        ans = current_small_sum
        
        for i in range(dist + 2, n):
            remove(nums[i - dist - 1])
            add(nums[i])
            ans = min(ans, current_small_sum)
            
        return nums[0] + ans