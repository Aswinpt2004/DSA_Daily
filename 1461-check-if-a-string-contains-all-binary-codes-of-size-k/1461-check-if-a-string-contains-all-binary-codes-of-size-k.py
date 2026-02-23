class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        
        if n < k:
            return False
        
        needed = 1 << k   
        seen = set()
        
        for i in range(n - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
            
            if len(seen) == needed:
                return True
        
        return len(seen) == needed