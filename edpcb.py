N, K = map(int, input().split())
h = tuple(map(int, input().split()))
INF = 1 << 32
dp = [INF] * N
dp[0] = 0
for i in range(N):
    for j in range(1, K + 1):
        if (i + j) < N:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))
            # print(i, j, h[i], h[i + j], dp)

print(dp[N - 1])
