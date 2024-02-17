from collections import deque


def decide(L):
    print(L)
    if len(L) > 1:
        op(L)


def opg(x, y, L):
    print("opg")
    res = (x * y) % 10
    L.appendleft(res)
    decide(L)


def opf(x, y, L):
    print("opf")
    res = (x + y) % 10
    L.appendleft(res)
    decide(L)


def op(L):
    x = L.popleft()
    y = L.popleft()
    opf(x, y, L)
    opg(x, y, L)


L = deque(range(10))
op(L)
