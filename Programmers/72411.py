import itertools
import collections

def solution(orders, course):
    answer = []
    for n in course:
        menu = []
        for o in orders:
            menu.extend(itertools.combinations(sorted(o), n))
        counter = collections.Counter(menu)
        if len(counter)!= 0 and max(counter.values())!=1 :
            max_value = max(counter.values())
            for el in zip(counter.keys(), counter.values()):
                if(el[1]>=max_value):
                    answer.append(''.join(sorted(el[0])))

    return sorted(list(set(answer)))
