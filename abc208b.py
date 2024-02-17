import math

P = int(input())
coins = []
for _ in range(10):
    coins.append(math.factorial(_ + 1))
count = 0
for coin in coins[::-1]:
    if P == 0:
        break
    elif P >= coin:
        m = P // coin
        P -= coin * m
        count += m
print(count)
