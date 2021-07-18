n = eval(input());s = list(map(int, input().split()))
print([False,any([str(x) == str(x)[::-1] for x in s])][all([x>0 for x in s])])