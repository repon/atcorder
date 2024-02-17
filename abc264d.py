S = list(input())
T = "atcoder"
ans = 0
for i in range(len(T)):
    S_i = S.index(T[i])
    while S_i != i:
        S[S_i], S[S_i - 1] = S[S_i - 1], S[S_i]
        S_i -= 1
        ans += 1
print(ans)
