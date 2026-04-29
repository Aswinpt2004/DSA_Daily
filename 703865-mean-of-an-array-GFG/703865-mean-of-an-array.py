class Solution:
    def findMean(self, arr):
        # code here 
        total = 0
        mean = 0
        length = len(arr)
        
        for n in arr:
            total = total + n
        
        mean = total / length
            
        return int(mean)
            
            