N, M = map(int, input().split())
A = "".join(input().split())
Flg = True
for i in range(N - M + 1):
    Aibin = int(A[i : (i + M)], 2)
    if Aibin == 0:
        print("NG")
        Flg = False
        break

if Flg:
    print("OK")
