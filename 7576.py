from collections import deque

col, row = map(int, input().split())
col += 2
row += 2
box = [[-1 for i in range(col)] for j in range(row)]
buff1 = deque()
buff2 = deque()
not_burn = 0
for i in range(1, row - 1):
    arr = list(map(int, input().split()))
    for j in range(1, col - 1):
        box[i][j] = arr[j - 1]
        if arr[j - 1] == 1:
            buff1.append([i, j])
        elif arr[j - 1] == 0:
            not_burn += 1


def test(cnt):
    day = 0
    if len(buff1) == (col - 2) * (row - 2):
        return 0
    while 1:
        while buff1:
            burn_tomoto = buff1.popleft()
            if box[burn_tomoto[0] - 1][burn_tomoto[1]] == 0:
                box[burn_tomoto[0] - 1][burn_tomoto[1]] = 1
                cnt -= 1
                buff2.append([burn_tomoto[0] - 1, burn_tomoto[1]])

            if box[burn_tomoto[0] + 1][burn_tomoto[1]] == 0:
                box[burn_tomoto[0] + 1][burn_tomoto[1]] = 1
                cnt -= 1
                buff2.append([burn_tomoto[0] + 1, burn_tomoto[1]])

            if box[burn_tomoto[0]][burn_tomoto[1] + 1] == 0:
                box[burn_tomoto[0]][burn_tomoto[1] + 1] = 1
                cnt -= 1
                buff2.append([burn_tomoto[0], burn_tomoto[1] + 1])

            if box[burn_tomoto[0]][burn_tomoto[1] - 1] == 0:
                box[burn_tomoto[0]][burn_tomoto[1] - 1] = 1
                cnt -= 1
                buff2.append([burn_tomoto[0], burn_tomoto[1] - 1])
        if not buff2:
            break
        day += 1
        while buff2:
            burn_tomoto = buff2.popleft()
            if box[burn_tomoto[0] - 1][burn_tomoto[1]] == 0:
                box[burn_tomoto[0] - 1][burn_tomoto[1]] = 1
                cnt -= 1
                buff1.append([burn_tomoto[0] - 1, burn_tomoto[1]])

            if box[burn_tomoto[0] + 1][burn_tomoto[1]] == 0:
                box[burn_tomoto[0] + 1][burn_tomoto[1]] = 1
                cnt -= 1
                buff1.append([burn_tomoto[0] + 1, burn_tomoto[1]])

            if box[burn_tomoto[0]][burn_tomoto[1] + 1] == 0:
                box[burn_tomoto[0]][burn_tomoto[1] + 1] = 1
                cnt -= 1
                buff1.append([burn_tomoto[0], burn_tomoto[1] + 1])

            if box[burn_tomoto[0]][burn_tomoto[1] - 1] == 0:
                box[burn_tomoto[0]][burn_tomoto[1] - 1] = 1
                cnt -= 1
                buff1.append([burn_tomoto[0], burn_tomoto[1] - 1])
        if not buff1:
            break
        day += 1
    if cnt != 0:
        return -1
    else:
        return day


print(test(not_burn))
