class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        S = 2 * m

        # Initial state for length = 2
        state = [0] * S
        for v in range(m):
            state[v] = v                  # up
            state[m + v] = m - 1 - v      # down

        # Transition matrix
        T = [[0] * S for _ in range(S)]

        # new_up[i] = sum(down[j]) for j < i
        for i in range(m):
            for j in range(i):
                T[i][m + j] = 1

        # new_down[i] = sum(up[j]) for j > i
        for i in range(m):
            for j in range(i + 1, m):
                T[m + i][j] = 1

        def mat_mul(A, B):
            n1, n2, n3 = len(A), len(B), len(B[0])
            C = [[0] * n3 for _ in range(n1)]
            for i in range(n1):
                for k in range(n2):
                    if A[i][k] == 0:
                        continue
                    x = A[i][k]
                    for j in range(n3):
                        C[i][j] = (C[i][j] + x * B[k][j]) % MOD
            return C

        def mat_pow(mat, power):
            size = len(mat)
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1

            while power:
                if power & 1:
                    res = mat_mul(res, mat)
                mat = mat_mul(mat, mat)
                power >>= 1
            return res

        def mat_vec_mul(mat, vec):
            size = len(mat)
            ans = [0] * size
            for i in range(size):
                s = 0
                for j in range(size):
                    s = (s + mat[i][j] * vec[j]) % MOD
                ans[i] = s
            return ans

        P = mat_pow(T, n - 2)
        final = mat_vec_mul(P, state)

        return sum(final) % MOD