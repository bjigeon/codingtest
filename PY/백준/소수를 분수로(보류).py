# #0.9(소수 부분의 자리수 만큼) 나누기 소수숫자 를 반올림 = 7

# #0.6142857

# #n,m= input().split("(")
# #print(n)
# #m=m.replace(")","")
# #print(m)

from fractions import Fraction

n =input()
print(n)
if("(") in n:
    f,s = n.split('(')
    fs = f+s.replace(")","")
    s=s.replace(")","")
    # print('문자')
    print('f',f)
    print('s',s)
    print('fs',fs)
    num = 9
    for i in range(len(s)-1):
        num =str(num) + str('9')
    cnt = float(num) / float(s)
    print('num',num)
    print('cnt',cnt)
    # print(Fraction(f*10)/)
    if(float(f) == 0):
        print(1,'/',int(cnt))
    else:
        fs = str(fs) + str(1)
        print(Fraction())
        
    #     print(Fraction())
else:
    print(Fraction(float(n)))
    # print('문자 없음')







# # num = 9
# # s='123'
# # for i in range(len(s)-1):
# #     num = str(num) + str('9')
# # print(num)

# # n=input()
# # f,s = n.split('(')
# # fs = f+s.replace(")","")
# # s=s.replace(")","")
# # print('문자')
# # print(f)
# # print(s)
# # print(fs)

# # print(float(0.))
# # print(float(0.6))

# # from fractions import Fraction


# # print(Fraction(42+1,70))


# from fractions import Fraction

# n =input()
# print(n)
# if("(") in n:
#     f,s = n.split('(')
#     fs = f+s.replace(")","")
#     s=s.replace(")","")
#     # print('문자')
#     print('f',f)
#     print('s',s)
#     print('fs',fs)
#     fs = str(fs) + 1
# else:
#     print(Fraction(float(n)))
#     # print('문자 없음')

# from fractions import Fraction


# fs = 0.6142857
# fs = str(fs) + str(1)
# print(Fraction(fs))
