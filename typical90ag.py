import math

H, W = map(int, input().split())
if H < 2 or W < 2:
    print(H * W)
else:
    print(math.ceil(H / 2) * math.ceil(W / 2))
