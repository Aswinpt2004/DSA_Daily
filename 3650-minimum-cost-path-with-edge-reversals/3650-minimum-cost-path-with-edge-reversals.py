import heapq

class Solution:
    def minCost(self, n, edges):
        # Build graph
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))        # normal edge
            graph[v].append((u, 2 * w))    # reversed edge via switch

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        # Min heap: (cost, node)
        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)

            if cost > dist[u]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1
