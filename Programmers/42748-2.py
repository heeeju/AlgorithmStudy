def solution(array, commands):
    return list(map(lambda num:sorted(array[num[0]-1:num[1]])[num[2]-1], commands))
