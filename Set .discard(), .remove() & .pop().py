n = int(input())
s = set(map(int, input().split()))
d = {"pop":s.pop, "remove":s.remove, "discard": s.discard}
for _ in range(int(input())):
    c = input().split()
    d[c[0]](int(c[1])) if len(c)>1 else d[c[0]]()
print(sum(s))