n = input()
f = int(input())
n = int(n[:-2] + '00')

while True:
    if n % f == 0:
        break
    n += 1
print(str(n)[-2:])

# n의 뒤 2자리 빼고 00을 붙인다
# 1씩 증가하면서 f 로 나누어 떨어지는 값의 뒤 2자리를 출력한다