S = input()
W = "chokudai"
WL = tuple([] for i in range(len(W)))
M = 10 ** 9 + 7
count = 0

for s in range(len(S)):
    for w in range(len(W)):
        if S[s] == W[w]:
            WL[w].append(s)


def dfs(slg, next):
    global count
    target = WL[next]
    if len(target) == 0:
        return
    if next == (len(W) - 1):
        for n in target:
            if n > slg:
                count = (count + 1) % M
    else:
        for n in target:
            if n > slg:
                dfs(n, next + 1)


if len(WL[0]) > 0:
    target = WL[0]
    for n in target:
        dfs(n, 1)

print(count)
