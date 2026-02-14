class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        i = 0 
        while i < n:
            j = i
            while j < n and s[j] == s[i]: j += 1
            res = max(res, j - i)
            i = j

        def two(x,y, exclude):
            i = 0
            mx = 0

            while i < n:
                if s[i] == exclude:
                    i += 1
                    continue
                m = {0: i -1}
                cx , cy = 0 , 0

                while i < n and s[i] != exclude:
                    if s[i] == x: cx += 1
                    else: cy += 1
                    key = cx - cy
                    if key in m: mx = max(mx, i - m[key])
                    else: m[key] = i
                    i += 1
            return mx

        res = max(res, two ('a','b','c'))
        res = max(res, two ('a','c','b'))
        res = max(res, two ('b','c','a'))


        m = {(0,0): -1}
        ca ,cb,cc = 0, 0, 0

        for i in range(n):
            if s[i] == 'a': ca += 1
            elif s[i] == 'b' : cb += 1
            else: cc += 1
            key = (ca - cb ,cb- cc)
            if key in m: res = max(res, i - m[key])
            else: m[key] = i

        return res

         


