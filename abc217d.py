import bisect
import array


def main():
    L, Q = map(int, input().split())
    # T = [0, L]
    T = array.array("i", [0, L])
    for q in range(Q):
        c, x = map(int, input().split())
        b = bisect.bisect(T, x)
        if c == 1:
            T.insert(b, x)
        else:
            ans = T[b] - T[b - 1]
            print(ans)


main()
