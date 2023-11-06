V, E = map(int, input().split())
dp_list = [[1000000000 for i in range(V + 1)] for j in range(V + 1)]

for i in range(E):
    V1, V2, cost = map(int, input().split())
    dp_list[V1][V2] = cost

for k in range(1, V + 1):
    for v1 in range(1, V + 1):
        if v1 == k:
            continue
        for v2 in range(1, V + 1):
            if v1 == v2 or v2 == k:
                continue
            straight = dp_list[v1][v2]
            pass_through = dp_list[v1][k] + dp_list[k][v2]
            min_cost = min(straight, pass_through)
            dp_list[v1][v2] = min_cost

min_cost = 1000000000
ck_list = [[0 for i in range(V + 1)] for j in range(V + 1)]
for v1 in range(1, V+1):
    for v2 in range(1, V+1):
        if v1 == v2:
            continue
        if ck_list[v1][v2] == 1:
            continue
        cost = dp_list[v1][v2] + dp_list[v2][v1]
        if cost >= 1000000000 or min_cost < cost:
            pass
        else:
            min_cost = cost
        ck_list[v1][v2] = 1
        ck_list[v2][v1] = 1
if min_cost == 1000000000:
    print(-1)
else:
    print(min_cost)
