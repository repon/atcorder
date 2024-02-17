from collections import defaultdict

H, W, N = map(int, input().split())
C = defaultdict(int)
for i in range(N):
    x, y = map(int, input().split())
    C[y] = x
setX = set()
setY = set()
for y, x in C.items():
    setX.add(x)
    setY.add(y)
setX = sorted(setX)
setY = sorted(setY)
res = []
for i in range(len(setY)):
    y = i + 1
    x = setX.index(C[setY[i]]) + 1
    res.append([x, y])

for p in res:
    print(p[0], p[1])
