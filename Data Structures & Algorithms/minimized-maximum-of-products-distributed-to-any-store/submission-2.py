import heapq

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Entries: (negative maximum, original quantity, stores assigned)
        heap = [(-q, q, 1) for q in quantities]
        heapq.heapify(heap)

        for _ in range(n - len(quantities)):
            _, q, stores = heapq.heappop(heap)

            stores += 1
            maximum = (q + stores - 1) // stores

            heapq.heappush(heap, (-maximum, q, stores))

        return -heap[0][0]