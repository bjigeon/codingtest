while True:
  try:
    a, b = map(int, input().split())
    print(a + b)
  except EOFError:
    break

#try 먼저 실행 while 때문에 계속 입력 받다가 에러(EOFError)가 
# 발생 했을때 except 문 실행