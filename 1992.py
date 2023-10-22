def div(start_row, start_col, size):
    if size == 1:
        if arr[start_row][start_col] == '1':
            return '1'
        else:
            return '0'

    a = div(start_row, start_col, size // 2)
    b = div(start_row, start_col + size // 2, size // 2)
    c = div(start_row + size // 2, start_col, size // 2)
    d = div(start_row + size // 2, start_col + size // 2, size // 2)


n, s, r = map(int, input().split())
n = 2 ^ n
arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = [None] * i

print(div(0, 0, n))
