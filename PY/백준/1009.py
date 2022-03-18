import sys
for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    c = pow(a,b,10)
    if c == 0: # 마지막 숫자가 0일떄  ==   if not c:
        print(c+10)
    else:
        print(c)