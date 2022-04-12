# baekjoon
# 01234567
# a b  c  d e  f  g  h  i j k  l  m n o  p  q  r  s  t  u  v  w  x  y  z
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

st = list(input())
re = [-1] * 26
for i in range(len(st)):
    for j in range(ord("a"),ord("z")+1):
        if(ord(st[i]) == j):
            if(re[j%97] != -1):
                continue
            else:
                re[j%97] = i
print(*re)