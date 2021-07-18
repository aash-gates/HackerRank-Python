from datetime import datetime

for i in range(int(eval(input()))):
    t1 = datetime.strptime(eval(input()), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(eval(input()), '%a %d %b %Y %H:%M:%S %z')
    print((abs(int((t1-t2).total_seconds()))))