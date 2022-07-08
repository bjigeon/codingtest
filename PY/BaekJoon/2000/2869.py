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

# import math
# import sys
# a,b,v = map(int,sys.stdin.readline().split())
# if a-b == 1:
#     print(v-b)
# else:
    # print(math.ceil(v/(a-b)))
    # print(round(v/(a-b)))



# (v-a) 에 (a-b) 로 며칠이 걸려야 도달할 수 있을까? 
# 2 1 5

# 5-2 1-2
# 3에 -1로


import math
import sys
a,b,v = map(int,sys.stdin.readline().split())
if a-b == 1:
    print(v-b)
else:
    print(1+math.ceil((v-a)/(a-b)))