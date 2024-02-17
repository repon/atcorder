N, Q = map(int, input().split())
L = []
LI = []
for i in range(N):
    tmp = list(map(int, input().split()))
    L.append(tmp.pop(0))
    LI.append(tmp)
for i in range(Q):
    x, y = list(map(int, input().split()))
    print(LI[x - 1][y - 1])
