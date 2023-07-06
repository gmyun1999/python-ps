from collections import deque

N, M = map(int, input().split())
dist = [[10005 for _ in range(M + 2)] for __ in range(N + 2)]
maze = [[0 for i in range(M + 2)] for j in range(N + 2)]
# 만약 지났으면 그 원소를 0으로 바꾸기.
# 1~N,  1~M
for i in range(1, N + 1):
    it = input()
    k = 1
    for j in it:
        maze[i][k] = int(j)
        k += 1
buff = deque()
dist[1][1] = 1
maze[1][1] = 2
if maze[1][2]:
    dist[1][2] = dist[1][1] + 1
    buff.append([1, 2])
if maze[2][1]:
    dist[2][1] = dist[1][1] + 1
    buff.append([2, 1])
new_dist = 1
while maze[N][M]:
    i, j = buff.popleft()
    if i == N and j == M:
        print(dist[N][M])
        break
    maze[i][j] = 2
    if maze[i - 1][j]:
        new_dist = dist[i][j] + 1
        if new_dist < dist[i - 1][j]:
            dist[i - 1][j] = new_dist
            buff.append([i - 1, j])
    if maze[i][j + 1]:
        new_dist = dist[i][j] + 1
        if new_dist < dist[i][j + 1]:
            dist[i][j + 1] = new_dist
            buff.append([i, j + 1])
    if maze[i + 1][j]:
        new_dist = dist[i][j] + 1
        if new_dist < dist[i + 1][j]:
            dist[i + 1][j] = new_dist
            buff.append([i+1, j])
    if maze[i][j - 1]:
        new_dist = dist[i][j] + 1
        if new_dist < dist[i][j - 1]:
            dist[i][j - 1] = new_dist
            buff.append([i, j - 1])

# 자기 앞,옆이랑 위아래를 봐야함.근데 현재 [i][j] 라고 했을때 i가 0이거나 N-1인경우는
# 위아래중 하나가 없음. 또한 현재j 가 0이나 m-1인경우는 앞뒤중 하나가 없음
# heap도 필요없을거같음
