class Solution:
    def removeDuplicates(self, arr):
        result = [arr[0]]   # First element always unique
        
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                result.append(arr[i])
        
        return result