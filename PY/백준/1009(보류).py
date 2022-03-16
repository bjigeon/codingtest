import sys
for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    print(str((a%10)**b)[-1])



# for i in range(int(input())):
#     a, b= list(map(int,input().split()))
#     print((a%10**b)%10)

# for i in range(30):
#     print(6**i)