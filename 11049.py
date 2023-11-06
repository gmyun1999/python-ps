"""
chain matrix 알고리즘이다.
이는 무조건 옆에꺼랑만 곱할수잇는거아닌가
->맞음
"""


def cal_matrix(i, j, k):
    if k == 1:
        val = input_data[i][0] * input_data[i][1] * input_data[i + 1][1]
    elif j == i:
        val = input_data[i][0] * input_data[i][1] * input_data[i + k][1] + matrix[j + 1][i + k]
    elif j == i + k - 1:
        val = matrix[i][j] + input_data[i][0] * input_data[i + k][0] * input_data[i + k][1]
    else:
        val = matrix[i][j] + matrix[j + 1][i + k] + input_data[i][0] * input_data[j][1] * input_data[i + k][1]

    if val < matrix[i][i + k]:
        matrix[i][i + k] = val


N = int(input())
input_data = [list(map(int, input().split())) for i in range(N)]
matrix = [[10000000000000 for _ in range(N)] for j in range(N)]

if N == 1:
    print(input_data[0][0] * input_data[0][1])
else:
    for k in range(1, N):  # k 는 인덱스간의 차이
        for i in range(0, N - k):  # N개탐색
            for j in range(i, i + k):
                cal_matrix(i, j, k)

    print(matrix[0][N - 1])
