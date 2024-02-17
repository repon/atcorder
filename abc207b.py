import math

A, B, C, D = map(int, input().split())
if D * C - B > 0:
    print(math.ceil(A / (C * D - B)))
else:
    print(-1)
