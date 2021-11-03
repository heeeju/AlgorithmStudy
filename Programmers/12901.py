def solution(a, b):
    day = 0
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    data = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    for i in range(a-1):
        day += days[i]
    day += b
    answer = data[(4+day)%7]
    return answer
