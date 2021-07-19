import numpy
numpy.set_printoptions(legacy=False)

arr = numpy.array([input().split() for _ in range(int(input().split()[0]))], int)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.around(numpy.std(arr, axis = None),decimals=11))