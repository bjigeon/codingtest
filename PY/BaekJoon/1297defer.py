from math import sqrt
import math

d,h,w = map(int,input().split())
sum = h+w

print( math.ceil(sqrt( (d**2) * (h**2) / (sum**2) ) ))
print( math.ceil(sqrt( (d**2) * (w**2) / (sum**2) ) ))
