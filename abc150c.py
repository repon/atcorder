from itertools import permutations


def main():
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    per = list(permutations(range(1, N + 1)))
    a = per.index(P)
    b = per.index(Q)
    print(abs(a - b))


main()
