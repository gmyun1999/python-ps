import heapq

num_ver, num_edge = map(int, input().split())
start = int(input()) - 1
adjlist = [[] for i in range(num_ver)]
closed = [False] * num_ver
dist = [10000000] * num_ver
dist[start] = 0
ver1 = 0
ver2 = 0
weight = 0
i = 0
while i < num_edge:
    ver1, ver2, weight = map(int, input().split())
    adjlist[ver1 - 1].append([ver2 - 1, weight])
    i += 1
heap = [[0, start]]
while heap:
    output = heap[0][1]
    heapq.heappop(heap)
    closed[output] = True
    for vert, weight in adjlist[output]:
        new_weight = weight + dist[output]
        if dist[vert] > new_weight:
            dist[vert] = new_weight
            heapq.heappush(heap, [new_weight, vert])
i = 0
while i < num_ver:
    if dist[i] == 10000000:
        print("INF")
    else:
        print(dist[i])
    i += 1
