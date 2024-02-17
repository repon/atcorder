N = int(input())
b_list = []
i = 1
while N > 0:
    if N & 1:
        b_list.append(i)
    N = N >> 1
    i += 1

for i in range(1 << len(b_list)):
    x = 0
    for j in range(len(b_list)):
        if i & (1 << j):
            x = x | 1 << (b_list[j] - 1)
    print(x)
