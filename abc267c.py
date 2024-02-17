N, M = map(int, input().split())
A = list(map(int, input().split()))
S_max = 0
S = 0
# k = 0のとき
for j in range(M):
    S += (j + 1) * A[j]
S_max = S

for k in range(1, N - M + 1):
    S = S - sum(A[k - 1 : k + M - 1]) + M * A[k + M - 1]
    if S_max < S:
        S_max = S

print(S_max)
