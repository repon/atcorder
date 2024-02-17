def main():
    N, Y = map(int, input().split())
    flag = False
    for x in range(N + 1):
        for y in range(N + 1 - x):
            z = N - x - y
            amount = x * 10 + y * 5 + z
            if flag:
                break
            elif amount == (Y // 1000):
                print(x, y, z)
                flag = True
                break
    if not flag:
        print(-1, -1, -1)


main()
