from __future__ import print_function
import numpy
n=int(raw_input())
a = numpy.array([raw_input().split() for _ in range(n)],int)
b = numpy.array([raw_input().split() for _ in range(n)],int)
m = numpy.dot(a,b)
print (m)