import array


N = int(input())
P = list(map(int, input().split()))
q = array.array("i", [0] * N)
# print(N, P, q)
# q = [0] * N
for i in range(N):
    # q.insert(P[i] - 1, i + 1)
    # print(q)
    q[P[i] - 1] = i + 1
print(*q)
