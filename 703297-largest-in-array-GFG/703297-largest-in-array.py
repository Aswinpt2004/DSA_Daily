class Solution:
    def largest(self, arr):
        
        largest = arr[0]
        
        for n in arr:
            if n > largest :
                largest = n
        
        return largest
