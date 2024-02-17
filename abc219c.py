from collections import defaultdict

X = input()
N = int(input())
S = []
l = []
for _ in range(N):
    s = input()
    S.append(s)
    l.append(len(s))
max_len = max(l)
L = defaultdict(str)
for s in S:
    num = ""
    for i in range(max_len):
        if len(s) <= i:
            num += "00"
        else:
            num += str(X.index(s[i]) + 1).zfill(2)
    L[int(num)] = s
L_sorted = sorted(L.items(), key=lambda x: x[0])
for l in L_sorted:
    print(l[1])
