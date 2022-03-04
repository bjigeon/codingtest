ysum = 0
msum = 0
n= int(input())
t = list(map(int,input().split()))
for i in range(n):
    
    na = int(t[i]/30)
    nna = int(t[i]%30)
    ysum+= (na*10)
    if(nna < 30):
        ysum+=10

    na = int(t[i]/60)
    nna=int(t[i]%60)
    msum+= (na*15)
    if(nna < 60):
        msum+= 15

if(msum == ysum):
    print('Y M ' + str(ysum))
elif(msum > ysum):
    print('Y '+ str(ysum))
elif(ysum > msum):
    print('M ' + str(msum))
