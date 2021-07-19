import numpy

N, M = list(map(int, input().split()))

my_array = numpy.array([ list(map(int, input().split())) for i in range(N) ])

print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(numpy.std(my_array, axis = None))