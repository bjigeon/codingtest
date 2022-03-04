sum = 0
st = list(input())
for i in range(len(st)):
    if(st[i] == 'A' or st[i] == 'B' or st[i] =='C'):
        sum += 3
    elif(st[i] == 'D'or st[i] =='E'or st[i] =='F'):
        sum += 4
    elif(st[i] == 'G' or st[i] =='H' or st[i] =='I'):
        sum += 5
    elif(st[i] == 'J' or st[i] =='K' or st[i] =='L'):
        sum += 6
    elif(st[i] == 'M' or st[i] =='N' or st[i] =='O'):
        sum += 7
    elif(st[i] == 'P'or st[i] =='Q' or st[i] =='R' or st[i] =='S'):
        sum += 8
    elif(st[i] == 'T' or st[i] =='U' or st[i] =='V'):
        sum += 9
    elif(st[i] == 'W' or st[i] == 'X' or st[i] == 'Y' or st[i] == 'Z'):
        sum += 10
print(sum)