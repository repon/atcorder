def main():
    N = int(input())
    p = []
    for _ in range(N):
        x, y = map(int, input().split())
        p.append((x, y))
    max_length = 0
    for i in range(N):
        for j in range(i + 1, N):
            _length = ((p[i][1] - p[j][1]) ** 2 + (p[i][0] - p[j][0]) ** 2) ** 0.5
            max_length = max(max_length, _length)
    print(max_length)


main()
