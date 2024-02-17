from collections import deque
import array
import sys

sys.setrecursionlimit(10000000)


def setans(res):
    global ans
    ans[res] = (ans[res] + 1) % 998244353


def opf(dA):
    x = dA.popleft()
    y = dA.popleft()
    f = (x + y) % 10
    dA.appendleft(f)
    if len(dA) == 1:
        setans(dA[0])
    else:
        print("opf", dA)
        op(dA)


def opg(dA):
    x = dA.popleft()
    y = dA.popleft()
    g = (x * y) % 10
    dA.appendleft(g)
    if len(dA) == 1:
        setans(dA[0])
    else:
        print("opg", dA)
        op(dA)


def op(dA):
    opf(dA)
    opg(dA)


N = int(input())
A = tuple(map(int, input().split()))
ans = array.array("i", [0] * 10)
dA = deque(A)
print(ans, N, A, dA)
op(dA)
for i in ans:
    print(i)
