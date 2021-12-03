info = sorted([int(input()) for i in range(9)])
num = sum(info)-100
i = 0
j = 8

while 1:
  if info[i]+info[j]==num:
    info[i] = 100
    info[j] = 100
    break
  elif info[i]+info[j] < num:
    i+=1
  else:
    j-=1


for i in info:
  if i != 100:
    print(i)
