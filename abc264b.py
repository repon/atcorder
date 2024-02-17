def p(RC):
    for row in RC:
        print(row)
    print()


RC = [[0] * 15 for i in range(15)]
# p(RC)
"""グリッドを塗る"""
for i in range(1, 8):
    """iが偶数なら黒(0)奇数なら白(1)"""
    Color = i % 2
    for r in range(i, 15 - i):
        for c in range(i, 15 - i):
            RC[r][c] = Color
    # p(RC)
# p(RC)

R, C = map(int, input().split())
res = "black" if RC[R - 1][C - 1] == 0 else "white"
print(res)
