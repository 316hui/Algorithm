import heapq
import sys

n = sys.stdin.readline()
n = int(n)
zero = 0
heap = []

for i in range(n):
    x = sys.stdin.readline()
    x = int(x)
    if x != 0:
        heapq.heappush(heap, x)
    else:
        zero += 1
        if len(heap) != 0:
            print(heap[0])
            heapq.heappop(heap)  # 가장 작은 원소를 힙에서 제거
        else:
            print(0)


