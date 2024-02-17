def main():
    N = int(input())
    S = str(input())
    counter = 0
    print(N, S)
    for i in range(1000):
        num = str(i).zfill(3)
        if num in S:
            print(num, S, S.count(num))
            counter += S.count(num)
    print(counter)


main()
