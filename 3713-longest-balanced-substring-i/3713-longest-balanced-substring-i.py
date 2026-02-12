from collections import defaultdict 
class Solution:
    def longestBalanced(self, s: str) -> int:
         
        n = len(s)
        result = 0
        for i in range(n):
            freq = defaultdict(int)
            for j in range(i , n):
                freq[s[j]]+= 1
                if len(set(freq.values()))==1:
                    result = max(result,j-i+1)

        return result