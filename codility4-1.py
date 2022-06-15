def solution(X, A):
    # write your code in Python 3.6
    dict1 = {}
    for i, j in enumerate(A):
        if j not in dict1:
            dict1[j] = 1 
        if len(dict1) == X:
            return i
    return -1