def solution(A):
    # Implement your solution here
    freqMap = {}
    for x in A:
        freqMap[x] = freqMap.get(x, 0) +1
    for x in A:
        if freqMap[x]%2 == 1:
            return x