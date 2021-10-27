def solution(board, moves):
    stack = []
    board.reverse()
    for i in range(len(board)):
        stack.append([])
    for row in board:
        for i, num in enumerate(row):
            if num != 0:
                stack[i].append(num)
    answer = 0
    bucket = []
    for move in moves:
        if len(stack[move-1]) != 0:
            doll = stack[move-1].pop()
            if len(bucket) != 0 and bucket[-1] == doll:
                answer += 2
                bucket.pop()
            else:
                bucket.append(doll)


    return answer
