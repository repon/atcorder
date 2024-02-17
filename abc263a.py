import collections

Card = list(map(int, input().split()))
c = collections.Counter(Card).most_common()
if len(c) == 2 and c[0][1] == 3 and c[1][1] == 2:
    print("Yes")
else:
    print("No")
