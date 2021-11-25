def solution(s):
    stack = []
    for ch in s:
        if len(stack) == 0 or ch != stack[-1]:
            stack.append(ch)
        elif ch == stack[-1]:
            stack.pop()

    return (min(len(stack), 1) + 1) % 2
