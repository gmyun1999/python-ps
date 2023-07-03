from collections import deque

vertex, edge, start = (map(int, input().split()))
start -= 1
adjlist = [[] for i in range(vertex)]
visited = [False] * vertex
i = 0
while i < edge:
    a, b = (map(int, input().split()))
    a = a - 1
    b = b - 1
    adjlist[a]
    adjlist[a].append(b)
    adjlist[b].append(a)
    i += 1
buff = deque()
buff.append(start)
# dfs
while buff:
    ver = buff.pop()
    if visited[ver] is True:
        continue
    visited[ver] = True
    print(ver + 1, end=' ')
    sorted_list = sorted(adjlist[ver], reverse=True)
    for i in range(len(sorted_list)):
        if visited[sorted_list[i]]:
            continue
        buff.append(sorted_list[i])
print()
# bfs
buff.append(start)
visited = [False] * vertex
while buff:
    ver = buff.popleft()
    if visited[ver] is True:
        continue
    visited[ver] = True
    print(ver + 1, end=' ')
    sorted_list1 = sorted(adjlist[ver])
    for i in range(len(sorted_list1)):
        if visited[sorted_list1[i]]:
            continue
        buff.append(sorted_list1[i])
