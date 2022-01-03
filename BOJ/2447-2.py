#메모리 38548KB
#시간 88ms
def draw_star(n):
  if n==1:
    return '*'
  else:
    answer = []
    minimi = draw_star(n//3)

    for m in minimi:
      answer.append(m*3)
    for m in minimi:
      answer.append(m+' '*len(m)+m)
    for m in minimi:
      answer.append(m*3)
    return answer

n = int(input())
print('\n'.join(draw_star(n)))
