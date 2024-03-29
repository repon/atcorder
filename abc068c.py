from collections import deque


def main():
    N, M = map(int, input().split())
    G = []
    for _ in range(0, N):
        G.append([])
    for _ in range(0, M):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        G[ai].append(bi)
        G[bi].append(ai)

    dist = []
    for _ in range(0, N):
        dist.append(-1)
    Q = deque()
    Q.append(0)
    dist[0] = 0
    while len(Q) > 0:
        i = Q.popleft()
        for j in G[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                Q.append(j)
    print(dist)
    if dist[N - 1] == 2:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


main()
