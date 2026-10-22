class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)
        for a, b, cost in flights:
            adj[a].append((b, cost))
        
        heap = [(0, 0, src)]
        jbound = defaultdict(lambda : float('inf'))
        while heap:
            currCost, jumps, node = heapq.heappop(heap)
            jbound[node] = min(jbound[node], jumps)
            if jumps > k+1:
                continue
            if node == dst:
                return currCost
            for nbr, cost in adj[node]:
                if jumps+1 > jbound[nbr]:
                    continue
                heapq.heappush(heap, (cost + currCost, jumps+ 1, nbr))
        
        return -1


