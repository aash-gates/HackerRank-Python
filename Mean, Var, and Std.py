import numpy
n,m = map(int,raw_input().split())
A = []
for _ in range(n):
    A.append(map(int,raw_input().split()))
A = numpy.array(A)
print numpy.mean(A,axis = 1)
print numpy.var(A,axis = 0)
print numpy.std(A)