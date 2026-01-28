import heapq

class Solution:
    def minCost(self, grid, k):
        m,n = len(grid), len(grid[0])

        cells = [(grid[i][j],i,j) for i in range(m) for j in range(n)]
        cells.sort()

        INF = 10**18
        dist = [[[INF] * (k +1)for _ in range(n)]for _ in range(m)]
        dist[0][0][0] = 0

        pq = [(0,0,0,0)]

        teleport_used = [0] * (k +1)

        while pq:
            cost,r,c,t = heapq.heappop(pq)

            if cost > dist[r][c][t]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            for nr, nc in ((r + 1, c),(r,c + 1)):
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + grid[nr][nc]
                    if new_cost < dist[nr][nc][t]:
                        dist[nr][nc][t] = new_cost
                        heapq.heappush(pq,(new_cost, nr, nc, t))

            if t < k:
                while teleport_used[t] < len(cells) and cells[teleport_used[t]][0] <= grid[r][c]:
                    _,x,y = cells[teleport_used[t]]
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][ t+ 1 ]= cost
                        heapq.heappush(pq, (cost ,x,y,t + 1))
                    teleport_used[t] += 1
        return -1