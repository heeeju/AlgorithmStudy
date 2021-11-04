def solution(a, b):
    day = b
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    data = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    for i in range(a-1):
        day += days[i]
    return data[(4+day)%7]
