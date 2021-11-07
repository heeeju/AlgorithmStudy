def solution(n):
    answer = ["수박"[i%2] for i in range(n)]
    return ''.join(answer)
