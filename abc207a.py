def main():
    Cards = list(map(int, input().split()))
    Cards.sort()
    print(sum(Cards[1:3:1]))


main()
