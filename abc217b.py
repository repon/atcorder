L = ["ABC", "ARC", "AGC", "AHC"]
S = []
for i in range(3):
    S.append(input())
L_S_and = set(L) ^ set(S)
print(L_S_and.pop())
