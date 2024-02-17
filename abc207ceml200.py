def main():
    N = int(input())
    sections = []
    for _ in range(N):
        t, l, r = list(map(int, input().split()))
        if t == 1:
            sections.append((l, r))
        elif t == 2:
            sections.append((l, r - 0.1))
        elif t == 3:
            sections.append((l + 0.1, r))
        elif t == 4:
            sections.append((l + 0.1, r - 0.1))

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            a, b = sections[i]
            c, d = sections[j]
            if max(a, c) <= min(b, d):
                ans += 1

    print(ans)


main()
