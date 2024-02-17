a = []
q = int(input())
for i in range(q):
    sp, sq = map(int, input().split())
    if sp == 1:
        a.append(sq)
    elif sp == 2:
        print(a[-sq])
