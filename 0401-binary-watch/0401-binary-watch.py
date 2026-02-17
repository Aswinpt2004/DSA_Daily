class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count(n):
            res = 0
            while n :
                res += n&1
                n >>= 1
            return res

        result = []
        for i in range(12):
            for j in range(60):
                if count(i)+count(j) == turnedOn :
                    hour = str(i)
                    min = (2 - len(str(j)))*'0' + str(j)
                    result.append(hour + ':' + min)
        
        return result