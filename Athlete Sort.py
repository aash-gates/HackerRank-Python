n,m = list(map(int,input().split()))
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
k = int(input())    
print("\n".join([" ".join(map(str, x)) for x in sorted(lst, key = lambda x: x[k])]))   