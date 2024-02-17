S = []
for i in range(3):
    S.append(input())
T = input()
res = ""
for i in range(len(T)):
    res += S[int(T[i]) - 1]
print(res)
