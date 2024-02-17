N = int(input())
A = tuple(map(int, input().split()))
X = int(input())
lenA = len(A)
sumA = sum(A)
d = X // sumA
modX = X - d * sumA
# print(N, A, X, lenA, sumA, d, modX)
sumAA = 0
countAA = 0
for i in A:
    sumAA += i
    countAA += 1
    if sumAA > modX:
        break
print(d * lenA + countAA)
