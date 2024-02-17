N = int(input())
A = list(map(int, input().split()))
s = sorted(A)[::-1]
sr = s[1]
r = A.index(sr)
print(r + 1)
