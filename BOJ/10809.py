alpha = [-1 for i in range(26)]
word = input()

for i, w in enumerate(word):
  idx = ord(w) - 97
  if alpha[idx] == -1:
    alpha[idx] = i

for i in range(26):
  print(alpha[i], end = ' ')
