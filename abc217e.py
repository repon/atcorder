import heapq
from collections import deque


def main():
    Q = int(input())
    A = []
    B = deque()
    for _ in range(Q):
        q = list(map(int, input().split()))
        if len(q) == 2:
            B.append(q[1])
        elif q[0] == 2:
            if len(A) == 0:
                print(B.popleft())
            else:
                print(heapq.heappop(A))
        else:
            for i in B:
                heapq.heappush(A, i)
            B.clear()


main()
