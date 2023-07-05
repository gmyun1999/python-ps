from collections import deque

n = int(input())
a = 1
order = []
result = []
for i in range(n):
    order.append(int(input()))
is_push = ['f'] * (n + 1)
is_push[0] = 'p'
# pop하거나 T돼있으면 할겡벗음
last_push = 0
last_pop = 0
# ptr은 마지막으로 push한 idx를 가리킨다.
dq = deque()
for i in order:
    if is_push[i] == 'f':
        for j in range(last_push + 1, i + 1):
            is_push[j] = 't'
            result.append('+')
        last_push = i
        result.append('-')
        is_push[i] = 'p'
        last_pop = i
    elif is_push[i] == 't':
        for j in range(last_pop - 1, i - 1, -1):
            if is_push[j] == 'p':
                continue
            is_push[j] = 'p'
            result.append('-')
        last_pop = i
    else:
        print("NO")
        a = 0
        break
if a ==1:
    print(*result)
