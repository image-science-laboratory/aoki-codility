def solution(A):
    # write your code in Python 3.6
    a = {}
    for i in A:
        if i not in a:
            a[i] = 1
    return len(a)