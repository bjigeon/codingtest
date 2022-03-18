# import sys
# a,b,v = map(int,sys.stdin.readline().split())
# h = 0
# cnt = 0
# if a == v:
#     print(1)
#     exit()
# while True:
#     if h >= v:
#         break
#     cnt += 1
#     h += (a-b)
#     print('h :',h)
# print(cnt) 

# import sys
# a,b,v = map(int,sys.stdin.readline().split())
# if a-b == 1:
#     print(v-b)
# else:
#     print(v-(a-b))

import math
import sys
a,b,v = map(int,sys.stdin.readline().split())
if a-b == 1:
    print(v-b)
else:
    print(math.ceil(v/(a-b)))