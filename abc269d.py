N = int(input())
hex_list = []
for i in range(N):
    hex_list.append(list(map(int, input().split())))
print(hex_list)
count = 0
rej_list = []
for lc in hex_list:
    if lc not in rej_list:
        x, y = lc
        adj_list = [
            [x - 1, y - 1],
            [x - 1, y],
            [x, y - 1],
            [x, y + 1],
            [x + 1, y],
            [x + 1, y + 1],
        ]
        rej_flag = True
        count_flag = True
        for adj in adj_list:
            print("adj,rej_list", adj, rej_list)
            if adj in rej_list:
                count_flag = False
        if count_flag:
            count += 1
            print("lc,count", lc, count)
        for cp in hex_list:
            if cp in adj_list:
                rej_list.append(cp)
                if rej_flag:
                    rej_flag = False
                    rej_list.append(lc)
                print("add rej_list", rej_list)
print(count)
