import itertools
import math


def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    d = 0
    for p in itertools.permutations(range(N), N):
        for s in range(N - 1):
            d += math.sqrt(
                (xy[p[s]][0] - xy[p[s + 1]][0]) ** 2
                + (xy[p[s]][1] - xy[p[s + 1]][1]) ** 2
            )
    print(d / math.factorial(N))


main()
