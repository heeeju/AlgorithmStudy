info = list(map(int, input().split()))
num = sum(info)-100
flag = 0

for i in range(len(info)-1):
  for j in range(i+1, len(info)):
    if flag == 1:
      break
    if info[i]+info[j] == num:
      info[i] = 100
      info[j] = 100
      flag = 1

for i in sorted(info)[:-2]:
  print(i)
