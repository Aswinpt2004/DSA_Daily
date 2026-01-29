class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10 ** 18

        dist = [[INF] * 26 for _ in range(26)]

        for i in range (26):
            dist[i][i] = 0

        for o,c,w in zip(original,changed , cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]      

        total_cost = 0
        for s, t in zip(source , target):
            if s == t:
                continue 

            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]
        
        return total_cost