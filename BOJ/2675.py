t = int(input())
for _ in range(t):
  n, s = input().split()
  for ch in s:
    print(ch*int(n), end='')
  print()
