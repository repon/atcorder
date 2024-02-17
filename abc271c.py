N = int(input())
A = list(map(int, input().split()))

if N <= 1:
    if A[0] == 1:
        print(1)
    else:
        print(0)
    exit()

A.insert(0, 0)

i = 1
k = 0

while True:
    print("head k,i", k, i)
    if i > N:
        print("if1")
        print(k)
        exit()
    elif A[i - 1] == k + 1:
        print("if2")
        k += 1
        i += 1
    elif A[i - 1] < k + 1:
        print("if3")
        add_k = (N - (i - 1)) // 2
        print(k + add_k)
        exit()
    else:
        print("if4")
        bw_k = A[i - 1] - 1 - k  # kからA[i-1]までの間に何冊必要か
        add_i = (N - i) // 2  # i-1~Nを売ったとき何冊買えるか？
        print("bw_k,add_i", bw_k, add_i)
        if bw_k == add_i:
            print("if4-1")
            print(A[i - 1])
            exit()
        elif bw_k > add_i:
            print("if4-2")
            print(k + add_i)
            exit()
        else:
            print("if4-3")
            k = A[i - 1]
            N -= 2 * bw_k
            i += 1
    print("foot k,i", k, i)
    # print("foot k,i,i - 1,A[i - 1]", k, i, i - 1, A[i - 1])
print(k)
