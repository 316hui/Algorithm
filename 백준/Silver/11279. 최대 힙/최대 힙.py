import heapq
import sys

n = sys.stdin.readline()
n = int(n)
heap = []

for i in range(n):
    x = sys.stdin.readline()
    x = -(int(x))

    if x != 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heap[0])
            heapq.heappop(heap)
