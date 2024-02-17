S = list(map(int, list(input())))
if S[0] == 0:
    pin = [
        S[7 - 1],
        S[4 - 1],
        S[8 - 1] | S[2 - 1],
        S[5 - 1],
        S[9 - 1] | S[3 - 1],
        S[6 - 1],
        S[10 - 1],
    ]

    count, flg = 0, 1

    for i in range(len(pin)):
        if pin[i] == flg:
            count += 1
            flg = 0 if flg == 1 else 1
            if count >= 3:
                print("Yes")
                exit()

print("No")
