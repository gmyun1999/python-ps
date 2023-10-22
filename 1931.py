# jobscheduling 문제로 전형적인 그리디 문제
import heapq

i = int(input())
heap = []
for _ in range(i):
    start, end = map(int, input().split())
    heapq.heappush(heap, (end, start))
cnt = 1
pre_end, pre_start = heapq.heappop(heap)
for _ in range(i - 1):
    end, start = heapq.heappop(heap)
    if start >= pre_end:
        cnt += 1
        pre_start = start
        pre_end = end
print(cnt)
