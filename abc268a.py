import collections

L = list(map(int, input().split()))
C = collections.Counter(L)
print(len(C))
