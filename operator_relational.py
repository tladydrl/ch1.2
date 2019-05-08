# 데이터 타입,, 객체.
# 객체: 값들을 저장하는 공간이다.  (변수라는건가?) (아니면 포인터를 객체라 부르는건가?)
# 객체: 값들을 참조하는 공간이다. a라는 이름으로 공간(2)를 가르킨다.
a = 2
a = 3  # 객체가 하나 더 만들어지고,

# 객체의 대소비교

print(1 > 3)  # 비교연산
print(isinstance(1>3, bool))
print(type(1>3))

print(1 >= 3)
print(2 <= 4)

print(1 == 3)
print(2 != 4)

# 파이썬; 복합 관계식 지원한다.
a = 6
print(0 < a and a < 10)  # 워닝 뜬다. 복합관계식 쓰기..
print(0 < a < 10)  # 파이썬에선 지원해준다.

# 수치형 이외의 다른 타입의 객체 비교
print('abcd' > 'abc')  # d가 하나더 있어서 더 크다.
print((1, 3, 3) > (1, 2, 6))  # 뒤에 하나더 크다. 앞이 우선순위가 높나보다.
print([1,2,3] > [1,2,2])  # 리스트 비교.

# 동질성 비교 : ==
# 동일성 비교 : is
a= 10
b = 20
c = a

print(a == b)
print(a is b)
print(a is c)
print(a == c)
# q. 배열에서는 동질성 동일성 어떻게되는가 is값? 배열의 값이 저장? 포인터?

# 논리식의 계산순서
print(True or 'logical')  # or 연산,, 1 or 0 = 0
print(False or 'logical')
print([] or 'logical')  # []은 false로 평가
print([10, 20] or 'logical')  #  [10,20]은 true로 평가.
print('operator' or 'logical')
print('' or 'logical')  # or 연산은 true아니면 false,, 불린으로 봐준다.
# 자바는 스트링이기때문에 에러 뜸.. 파이썬은. 평가해주려함.

print(None or 'logical')  # or 연산은 true아니면 false,, 불린으로 봐준다.
print(None or [])  # 위에 출력하기 위해 None 을 평가함, []출력..

s = 'Hello World'
s and print(s) # s는 트루니까 뒤까지 출력.
print(0)
s = ''
s and print(s)  # 아무것도 출력되지않느다.
print(1)
print(s)
print(2)

# 비트연산.. 2진수로 계산..
# 비트를 하나씩 계산한다.
# 이미지처리나,,
# 나누기 곱하기, 쉬프트,
# 비트연산으로 나누기 곱하기.,,,

#

























