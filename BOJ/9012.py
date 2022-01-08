n = int(input())
for _ in range(n):
  stack = []
  flag = 1
  info = input()
  for i in info:
    if i == '(':
      stack.append(1)
    else:
      if len(stack) != 0:
        stack.pop()
      else:
        flag = 0
  if flag == 0 or len(stack) != 0:
    print('NO')
  else:
    print('YES')
