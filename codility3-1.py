def solution(X, Y, D):
    # write your code in Python 3.6
    ans = (Y - X) // D + 1
    if (Y - X) % D == 0:
        ans -= 1
    
    return ans