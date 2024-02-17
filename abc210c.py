from collections import defaultdict

N, K = map(int, input().split())
C = list(map(int, input().split()))
colors = defaultdict(int)

for i in range(0, K):
    colors[C[i]] += 1

ans = len(colors)
kind = len(colors)

for i in range(K, N):
    colors[C[i]] += 1
    if colors[C[i]] == 1:
        kind += 1
    colors[C[i - K]] -= 1
    if colors[C[i - K]] == 0:
        kind -= 1
    ans = max(ans, kind)

print(ans)
