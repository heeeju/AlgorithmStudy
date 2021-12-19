T = int(input())
answer = []
for _ in range(T):
  str = list(input())
  if len(answer) != len(str):
    answer = str
  else:
    for i in range(len(str)):
      if answer[i] != str[i]:
        answer[i] = "?"
print(''.join(answer))
