s = input()
if s[0] == "<" and s[1 : (len(s) - 1)] == "=" * (len(s) - 2) and s[-1] == ">":
    print("Yes")
else:
    print("No")
