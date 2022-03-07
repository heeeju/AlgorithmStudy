import sys
input = sys.stdin.readline

n = int(input())
info = []
for _ in range(n):
  x, y = map(int, input().split())
  info.append([x, y])

for el in sorted(info, key = lambda x : (x[1], x[0])):
  sys.stdout.write(str(el[0])+' '+str(el[1])+'\n')
