T = int(input())
for _ in range(T):
  info = list(map(int, input().split()))
  mean = sum(info[1:])/info[0]

  student = [1 for i in info[1:] if i > mean]
  print('%.3f' %(sum(student)/(len(info)-1) * 100), '%', sep='')
