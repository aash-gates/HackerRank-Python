N = int(input())
A = [0,1]
for i in range(2,N): A.append(A[i-1]+A[i-2])        
print([a*a*a for a in A][:N])