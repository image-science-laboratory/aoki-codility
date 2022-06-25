N = int(input())
S = str(input())
W = list(map(int, input().split()))
A = []
count1 = 0
for i, j in enumerate(W):
  A.append([int(S[i]), j])
  if S[i] == str(1):
    count1 += 1
A = sorted(A, key=lambda x: x[0], reverse=True)
A = sorted(A, key=lambda x: x[1])
ans = count1
for k in A:
  if k[0] == 0:
    count1 += 1
    if count1 > ans:
      ans = count1
  else:
    count1 -= 1
print(ans)