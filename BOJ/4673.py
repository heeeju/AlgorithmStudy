answer = [0 for i in range(10000)]
check = [0 for i in range(10000)]

for i in range(1, 10000):
  if check[i]==0:
    target = i
    while 1:
      check[target] = 1
      target += sum(map(int, list(str(target))))
      if target >= 10000 or check[target] != 0:
        break
      answer[target] = 1

for i in range(1, 10000):
  if answer[i] == 0:
    print(i)
