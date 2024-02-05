def solution(N):
    # Implement your solution here
    stack = []
    res = 0
    while N > 0:
        stack.append(N%2)
        N = N//2
    count = 0
    for i in range(len(stack)):
        if stack[i] == 0 and count == 0:
            continue
        if stack[i] == 1 and count > 0:
            res = max(res, count-1)
            count = 0
        count +=1
    return res