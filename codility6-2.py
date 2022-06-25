def solution(A):
    # write your code in Python 3.6
    a = [-10**5] * 3
    b = [0] * 2
    for i in A:
        if a[0] < i:
            a[0] = i
            a = sorted(a)
        if b[1] > i:
            b[1] = i
            b = sorted(b)
    if b[0]*b[1]*a[2] > a[0]*a[1]*a[2]:
        return b[0]*b[1]*a[2]
    return a[0]*a[1]*a[2]