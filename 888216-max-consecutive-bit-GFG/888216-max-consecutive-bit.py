class Solution:
    def maxConsecBits(self, arr):
        count = 1
        max_count = 1 
        
        for i in range(1,len(arr)):
            if arr[i] == arr[i -1]:
                count = count + 1
                
            else:
                count = 1
            
            if count > max_count:
                max_count = count
                
        return max_count
        
        