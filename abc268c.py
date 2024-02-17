import collections

N = int(input())
p = list(map(int, input().split()))
# 商品ごとの、喜べる回す回数を収納
pp = []

for j in range(N):
    pp.append((p[j] - j - 1) % N)
    pp.append((p[j] - j) % N)
    pp.append((p[j] - j + 1) % N)

print(collections.Counter(pp).most_common()[0][1])
