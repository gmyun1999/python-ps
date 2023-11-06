N = int(input())
dp = [[0 for i in range(3)] for j in range(N + 1)]
for N in range(N):
    dp[N][0], dp[N][1], dp[N][2] = map(int, input().split())
for i in range(1, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]
print(min(dp[N][0], dp[N][1], dp[N][2]))
