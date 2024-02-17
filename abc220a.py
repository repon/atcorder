A, B, C = map(int, input().split())
d_b = B // C
ans = d_b * C
# print(A, B, C, d_a, d_b)
if A <= ans <= B:
    print(ans)
else:
    print(-1)
