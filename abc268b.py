S = input()
T = input()

if len(S) < 1:
    print("Yes")
elif len(S) > len(T):
    print("No")
else:
    if S == T[0 : len(S)]:
        print("Yes")
    else:
        print("No")
