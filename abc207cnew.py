def hasEqual(A, B):
    at, a1, a2 = A
    bt, b1, b2 = B
    if (a1 <= b1 < a2) or (a1 < b2 <= a2) or (b1 <= a1 < b2) or (b1 < a2 <= b2):
        return 1
    elif a1 == b2 and at < 3 and (bt % 2 == 1):
        return 1
    elif a2 == b1 and (at % 2 == 1) and bt < 3:
        return 1
    else:
        return 0


def main():
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    counter = 0
    for i in range(N):
        for j in range(i + 1, N):
            counter += hasEqual(data[i], data[j])
    print(counter)


main()
