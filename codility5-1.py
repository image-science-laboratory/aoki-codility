def solution(A):
    # write your code in Python 3.6
    count = 0
    ans = 0
    for i in A:
        if i == 0:
            count += 1
        else:
            ans += count
            if ans > 10**9:
                return -1
    return ans