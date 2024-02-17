X = input()
d_flg = True
if (X[0] == X[1]) & (X[1] == X[2]) & (X[2] == X[3]):
    print("Weak")
    d_flg = False
if (
    (((int(X[0]) + 1) == int(X[1])) or (X[0] == "9" and X[1] == "0"))
    and (((int(X[1]) + 1) == int(X[2])) or (X[1] == "9" and X[2] == "0"))
    and (((int(X[2]) + 1) == int(X[3])) or (X[2] == "9" and X[3] == "0"))
):
    print("Weak")
    d_flg = False

if d_flg:
    print("Strong")
