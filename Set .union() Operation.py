eng = set()
fre = set()
n = raw_input()
for i in raw_input().split(' '):
  eng.add(i)
m = raw_input()
for i in raw_input().split(' '):
  fre.add(i)
sol = eng.union(fre)
print len(sol)


Problem solution in Python 3 programming.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())

s1 = set(l)
s2 = set(k)

print(len(s1.union(s2)))