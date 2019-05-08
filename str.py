# 한 줄 문자열

s = ''
str1 = 'Hello World'
str2 = "Hello World"  # 큰따옴표 작은따옴표 차이는 없는데 보통 문자열은 '' 쓴다.

print(type(s), type(str1), type(str2))
print(isinstance(str1, str))

# 여러줄 문자열
str3 = """ABC
DEF
가나다라마바사
아자차카타파하"""
print(str3)  # 여러줄문자열?

# 여러줄 주석 => 여러줄 문자열을 사용한다.
1  # 1하고 넘어가는 거랑 같다. , 1이란 객체는 18번 라인에서 사라진다.
"""  # 이거는 주석이 아니다.
dwdwsdw
dwdwdw
dwdwdwd
""" # 스트링 객체가 만들어진 다음에 사라진다.

# escape(\)
print('hello\nworld\n')
print("I Say \"HelloWorld\"")
print('I Say "HelloWorld"')
print('She\'s Mom')
print("She's Mom")
print("둘리\t010-0000-0000")

# 문자열 연산
str1 = "First String"
str2 = "Second String"


str4 = str1*3  # str1을 세번곱합.
print(str4)

#인덱싱
print(str1[0], str1[2], str1[4])

#슬라이싱(slicing)  # 잘라내는것..
str5 = str2[2:5] # 3번째부터 5번째까지 짤라내는것이다.
print(str5)  # str5 라는 새로운 객체가 생긴것이다. 짤라진것.
print(str2[2:]) # 끝까지 잘라내는것이다.

# 연결(+), + 는 생략이 가능하다.
str3 = str1 + ' ' +str2
print(str3)
str6 = 'Hello' '-' 'World'  # 리터럴 상수로 할때는 + 생략가능하다, 변수로 할때는 생략 불가능하다.
print(str6)

# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다.
name = '길동'
age = 40
#print(name + age) # 예외가 발생했는데,,, 파이썬이 막아논것이다.
print(name + str(age))  # 클래스 배우면 왜안되는지 배운다. 자바?

# len() 함수
print(len(str2))

# in, not in 연산자 (시퀀스에 지원)
# in은 들어있는지 확인..
print("S" in str2)
print("S" not in str2)

# 문자열 객체는 변경할 수 없다. (immutable)
# str1[0] = 'f'
print(str1)  # 0이면 성공적으로 파이썬이 실행됬다. 1이면 뭔가 문제가 있다.

# python str.py  ,, 리턴값을 준다. 1이면 정상적으로 실행되지않음,, 문법이나 ,안되는것..
# 나중에 예외를 받아낼 수 있다.

# formating(서식) - tuple  # 나는 이런 폼으로 문자열을 나타내겠다?
f = "name => %s, age => %d"  # 자리에다가 문자열, 정수형 숫자를 넣겠다.
print(f)
print( f % ('둘리', 10))
print( f % ('또치', 20))

# formating(서식) - format() 함수
name = "마이콜"
age = 30
print("name => " +name + ", age => " + str(age))  # age가 스트링이 아니라서 에러가 뜸.
print("name => " +name + ", age => " + format(age, "d"))  # age가 스트링이 아니라서 에러가 뜸.
print("name => " + format(name, "s") + ", age => " + format(age, "d"))  # age가 스트링이 아니라서 에러가 뜸.
# &랑, format 사용했음.
#지금까지 쓴것: 전역함수
#이제: 객체함수. ex) format

# 대소문자 관련 객체함수  # str 파일보면 string 관련... 예제.
s = "i like Python"
print(s.upper())
print(s.lower())
print(s.swapcase())  # 대문자랑 소문자랑 스위칭 해준다.
print(s.capitalize()) # 맨 앞 문자만 대문자.
print(s.title())  # 각 단어의 맨 앞만 대문자.

# 검색 관련 객체함수  #있는지 없는지 확인..
s = "I Like Python, I Like Java Also"  # 한글도 다 된다.
print(s.count("Like")) # Like라는 문자의 개수 출력.
print(s.find("Like")) # 문자열에서 이 문자가 처음나오는 위치의 인덱스.. 0,1,2.
print(s.find("Like", 5)) # 문자 \ 5번째부터 찾음
print(s.find("JavaScript"))  # 찾지 못했을때 -1..
print(s.rfind("Like")) #


# 내일 편집 치환 , 정렬,, 예외. -1//
# 검색해서 찾을 수 있도록. 스트링..
# 리스트,, 튜플.












