# import sys
# l = [int(sys.stdin.readline()) for i in range(int(input()))]
# l.sort()
# for i in range(len(l)):
#     print(l[i])

import sys
l = []
for i in range(int(input())):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in range(len(l)):
    print(l[i])
