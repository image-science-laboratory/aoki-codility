def solution(N, A):
    # write your code in Python 3.6
    ans = [0] * N
    max_ans = 0
    max_ans1 = 0
    for j in A:
        if j <= N:
            if ans[j-1] < max_ans1:
                ans[j-1] = max_ans1 + 1
            else:
                ans[j-1]  += 1
            if max_ans < ans[j-1]:
                max_ans = ans[j-1]
        else:
            max_ans1 = max_ans

    for i in range(len(ans)):
        if ans[i] < max_ans1:
            ans[i] = max_ans1
    return ans