scores = []
for _ in range(5):
  scores.append(max(40,int(input())))

print(int(sum(scores)/5))
