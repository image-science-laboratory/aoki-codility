def solution(A):
    # write your code in Python 3.6
    a = {}
    ans = 1
    for i in A:
        if i not in a:
            a[i] = 1
    while ans < 10**6:
        if ans not in a:
            return ans
        ans += 1