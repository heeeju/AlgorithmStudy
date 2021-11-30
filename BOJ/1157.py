from collections import Counter

answer = []
str = input().upper()
counter = Counter(str)
max_val = max(list(counter.values()))

for k, v in zip(counter.keys(),counter.values()):
  if v == max_val:
    if len(answer) == 0:
      answer.append(k)
    else:
      answer = ['?']
      break

print(answer[0])
