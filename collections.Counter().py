from collections import Counter
X = eval(input())
S = Counter(list(map(int,input().split())))
N = eval(input())
earnings = 0
for customer in range(N):
    size, x_i = list(map(int,input().split()))
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print(earnings) 