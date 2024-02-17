N, P, Q, R = map(int, input().split())
A = tuple(map(int, input().split()))
S = [P, Q, R]
x = 0
for j in range(3):
    for x_i in range(x, N):
        for y_i in range(x_i + 1, N):
            T = sum(A[x_i:y_i])
            if T == S[j]:
                if j == 2:
                    print("Yes")
                    exit()
                else:
                    x = y_i
                    break
        else:
            continue
        break

print("No")
