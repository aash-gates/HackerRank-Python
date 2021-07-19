from itertools import *

K, M = list(map(int, input().split()))
N = []

for _ in range(K):
     N.append(map(int, input().split())[1:])        
MAX = -1
for i in product(*N):
    MAX = max(sum([x**2 for x in i])%M, MAX)
    
print(MAX)  