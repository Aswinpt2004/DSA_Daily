class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)[::-1]
        if str(x) == a :
            return True
        else:
            return False
solution = Solution() 