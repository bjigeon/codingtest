# from math import sqrt
# import math

# d,h,w = map(int,input().split())
# sum = h+w

# print( math.floor(sqrt( (d**2) * ((h**2) / (sum**2) ) )))
# print( math.floor(sqrt( (d**2) * ((w**2) / (sum**2) ) )))


import math
d,h,w = map(int,input().split())
sum = h + w
print(math.floor( (d**2) * (h/sum)))
print(math.floor( (d**2) * (w/sum)))


print(math.sqrt(math.floor( (d**2) * (h/sum))))
print(math.sqrt(math.floor( (d**2) * (w/sum))))
