S = input()

base = ["oxx", "xxo", "xox"]

s_len = len(S)
s_quo = s_len // 3
s_mod = s_len % 3

flag = False
for b in range(3):
    t = base[b] * s_quo + base[b][0:s_mod]
    if t == S:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
