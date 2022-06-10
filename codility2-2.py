def solution(A):
    # write your code in Python 3.6
    a = {}
    for i in A:
        if str(i) in a:
            a[str(i)] += 1
        else:
            a[str(i)] = 1
    ans = [k for k, b in a.items() if b % 2 == 1]
    return int(ans[0])