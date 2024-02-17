import collections


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_counter = collections.Counter(A)
    count = combinations_count(N, 2)
    for i in A_counter.values():
        if i >= 2:
            count -= combinations_count(i, 2)
    print(count)


def combinations_count(n, r):
    return n * (n - 1) // r


main()
