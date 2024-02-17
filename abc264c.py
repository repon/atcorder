H1, W1 = map(int, input().split())
A = []
for i in range(H1):
    A.append(list(map(int, input().split())))
H2, W2 = map(int, input().split())
B = []
for i in range(H2):
    B.append(list(map(int, input().split())))
for RowB in range(1 << H1):
    for ColB in range(1 << W1):
        OpeA = []
        for i in range(H1):
            if RowB >> i & 1:
                Row = []
                for j in range(W1):
                    if ColB >> j & 1:
                        Row.append(A[i][j])
                OpeA.append(Row)
        if OpeA == B:
            print("Yes")
            exit()
print("No")
