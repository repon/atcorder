N = int(input())
h = tuple(map(int, input().split()))
dp = [0] * N
for i in range(N):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = dp[i - 1] + abs(h[i] - h[i - 1])
    else:
        a1 = dp[i - 1] + abs(h[i] - h[i - 1])
        a2 = dp[i - 2] + abs(h[i] - h[i - 2])
        dp[i] = a1 if a1 < a2 else a2

print(dp[N - 1])
