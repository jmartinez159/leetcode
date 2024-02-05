def solution(A, K):
    # Implement your solution here
    if len(A) == 0 or K%len(A) == 0:
        return A
    res = []
    K = K%len(A)
    for i in range(len(A)):
        res.append(0)
    for i in range(len(A)):
        res[(i+K)%len(A)] = A[i]
    return res