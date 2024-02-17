def main():
  n = int(input())
  a = list(map(int, input().split()))
  if sum(a) == n * (n-1) / 2: print("Yes")
  else: print("No")
main()