def main():
    N = int(input())
    ll = list(map(int, input().split()))
    ll.sort()
    count = 0
    for i in range(N):
        for j in range(i):
            for k in range(j):
                print(i)
                # print(k, j, i, ll[k], ll[j], ll[i])
                if ll[k] != ll[j] and ll[i] != ll[j] and ll[k] + ll[j] > ll[i]:
                    count += 1
    print(count)


main()
