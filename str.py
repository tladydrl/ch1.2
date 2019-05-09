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
"""  # 스트링 객체가 만들어진 다음에 사라진다.

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

str4 = str1 * 3  # str1을 세번곱합.
print(str4)

# 인덱싱
print(str1[0], str1[2], str1[4])

# 슬라이싱(slicing)  # 잘라내는것..
str5 = str2[2:5]  # 3번째부터 5번째까지 짤라내는것이다.
print(str5)  # str5 라는 새로운 객체가 생긴것이다. 짤라진것.
print(str2[2:])  # 끝까지 잘라내는것이다.

# 연결(+), + 는 생략이 가능하다.
str3 = str1 + ' ' + str2
print(str3)
str6 = 'Hello' '-' 'World'  # 리터럴 상수로 할때는 + 생략가능하다, 변수로 할때는 생략 불가능하다.
print(str6)

# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다.
name = '길동'
age = 40
# print(name + age) # 예외가 발생했는데,,, 파이썬이 막아논것이다.
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
print(f % ('둘리', 10))
print(f % ('또치', 20))

# formating(서식) - format() 함수
name = "마이콜"
age = 30
print("name => " + name + ", age => " + str(age))  # age가 스트링이 아니라서 에러가 뜸.
print("name => " + name + ", age => " + format(age, "d"))  # age가 스트링이 아니라서 에러가 뜸.
print("name => " + format(name, "s") + ", age => " + format(age, "d"))  # age가 스트링이 아니라서 에러가 뜸.
# &랑, format 사용했음.
# 지금까지 쓴것: 전역함수
# 이제: 객체함수. ex) format

# 대소문자 관련 객체함수  # str 파일보면 string 관련... 예제.
s = "i like Python"
print(s.upper())
print(s.lower())
print(s.swapcase())  # 대문자랑 소문자랑 스위칭 해준다.
print(s.capitalize())  # 맨 앞 문자만 대문자.
print(s.title())  # 각 단어의 맨 앞만 대문자.

# 검색 관련 객체함수  #있는지 없는지 확인..
s = "I Like Python, I Like Java Also"  # 한글도 다 된다.
print(s.count("Like"))  # Like라는 문자의 개수 출력.
print(s.find("Like"))  # 문자열에서 이 문자가 처음나오는 위치의 인덱스.. 0,1,2.  # 나오는 위치 리턴해준다.
print(s.find("Like", 5))  # 문자 \ 5번째부터 찾음
print(s.find("JavaScript"))  # 찾지 못했을때 -1..
print(s.rfind("Like"))  # 반대로 찾음

# 내일 편집 치환 , 정렬,, 예외. -1//
# 검색해서 찾을 수 있도록. 스트링..
# 리스트,, 튜플.

print(s.index("Like"))  # 위치출력
# 발견하지 못하면 예외가 발견한다.

# try:
# print(s.index("JavaScript")) # 얘는 못찾으면 익셉션 나온다. # find는 못찾으면 -1리턴,, 에러발생x
# 예외발견하기: try,

# 예외 발견한 원인 알기..
print('ok')

print(type(format(10, "d")))  # 스트링객체네

print(s.rindex("Like"))

print(s.startswith('I Like'))  # 시작하는게 이걸로 시작되는지 확인한다.
print(s.startswith('I Like', 2))  # 세번째가 아이 라이크로 시작하는가.
print(s.startswith('Like', 2))  # 세번째가 라이크로 시작하는가.
print(s.endswith('Also'))  # 끝나는게 이걸로 확인.
print(s.endswith('Java', 0, 26))  # 범위 정해줌. 0부터 26 바로앞까지
# 나중에 찾아보면 거의다 있다.

# 충분히 웹프로그램 이정도로 충분

# 편집과 치환
s = '      spam and ham   '
print(s.strip())  # 양쪽에 스페이스 제거해줌.
print('--' + s.strip() + '--')
print('--' + s.rstrip() + '--')  # 오른쪽 제거
print('--' + s.lstrip(' ') + '--')  # 왼쪽 제거

# 이것을 왜 하느냐..
# ex)   email, password 에서 왼족오른쪽 공백..
# email <= "a@gmail.com  "  # 스페이스.. 변수로만 다룸.
# db.insert(email, pwd)  # db에 스페이스 있는채로들어감.
# db.insert(email.strip(), pwd.strip()) ..

s = '<><abc><><defg><>'
print('--' + s.strip(' ') + '--')  # 파라미터 없으면 ' '를 지운다.
print('--' + s.strip('<>') + '--')  # '<>' 는 < 지우고 > 지운다. 양쪽으로

s = 'Hello Java Java Java Python'
print(s.replace('Java', 'Python'))  # 자바를 모두 파이썬으로 바꿔준다.

# 정렬
s = 'King and Queen'  # 롸이트 레프트 센터 얼라인,, 문자를 보여줄때...
print('---' + s.center(30) + '---')  # 60은..  # 60 스페이스를 마련하고, 그중에 가운데다가 놓겠다.
print('---' + s.ljust(30) + '---')  # 60은..  # 30 스페이스를 마련하고, 그중에 왼쪽다가 놓겠다.
print('---' + s.rjust(30) + '---')  # 60은..  # 30 스페이스를 마련하고, 그중에 오른쪽에다가 놓겠다.

# 분리. (생각보다 많이씀)
s = 'spam and ham'  # 두 스트링으로 분리하겠다.  리턴은 배열 아니면 튜플이 나와야 한다.
r = s.split(' and ')  # and를 가지고, 두 단어를 분리하겠다. 단어가 두개가 나온다.
print(r, type(r))  # 리스트 반환.. 리스트 연속공간. 레퍼렌싱..

s = 'one:two:three:four'  # 개별적인 문자로 분리하고싶다면,,
r = s.split(':')
print(r)  # 리스트의 크기는 정해지나?

# 결합  # 문자열이 들어있는 리스트를 결합해준다.
s = ','.join(r)  # r 문자열을 .로 합쳐라.
print(s)
s = ':'.join(r)  # r 문자열을 .로 합쳐라.
print(s)

r = s.split(':', 2)  # 두개 만 분리해주고, 나머지는 한꺼번에 뭉치로 준다.
print(r)

r = s.rsplit(':', 2)  # 두개 만 분리해주고, 나머지는 한꺼번에 뭉치로 준다.
print(r)

lines = """1st line
2nd line
3rd line
4rh line
"""

print(lines)

lines = """1st line
2nd line
3rd line
4rh line
"""  # 개행 없게하기.
print(lines + '--')

r = lines.split('\n')  # 빈 문자열 무시하지 않는다.
print(r)
r = lines.splitlines()  # 빈문자열 무시할 수 있다. 한줄씩 나누기.
print(r)

r = lines.split('\n')  # 빈 문자열 무시하지 않는다.

# 결합  # 문자열이 들어있는 리스트를 결합해준다.
s = ','.join(r)  # r 문자열을 .로 합쳐라.
print(s)
s = ':'.join(r)  # r 문자열을 .로 합쳐라.
print(s)

# 판별. ,,
# "1234" , "abcd" 등..
# 그 뒤 리스트,, 연산, 객체함수들.
print("1234".isdigit())
print("abcd".isalpha())

print("1234d".isalpha())  # 1234 있어서 폴스
print("abcd1".isdigit())  # abcd 있어서 폴스..  완전숫자거나 완전 알파인지 판별한다.

print("abcdef".islower())  # 문자중,, 소문자이냐
print("ABCDEF".isupper())  # 문자중,, 대문자이냐

print(" ".isspace())
print("".isspace())  # 폴스나온다
print("\n".isspace())  # 개행문자 스페이스로 본다.
print("\t".isspace())  # 탭도 스페이스로 본다.
# 이것들 다 책에 나와있는 내용이다.
# 이런기본으로.. 다음주에 크롤링... 이런것들 일부 나올것이다.. 응용프로그램 만들기..
# 지겹더라도 한번 쳐보기.
# 다음주 수요일 부터 이런거 기반으로..

# 0 채우기
# '20190509-0001'  # 등.. 날짜에 주문번호 넣기..
print(str(1).zfill(5))  # 스트링 객체함수.. str()  # 5자리 0으로 채움.
print(str(9234).zfill(5))  # 스트링 객체함수.. str()  # 5자리 0으로 채움.

# formating(서식)    # 위의 % 랑 format이랑 다름.
f = "name:{}, age:{}"  # {0} {1} 생략.
s = f.format("둘리", 10)
print(s)

f = "name:{1}, age:{0}"  # 인덱스로 주기... 안주면 파라미터 순서대로 들어감. 순서지정.
s = f.format(10, "둘리")
print(s)
print("name:{0}, age:{1}".format("둘리", 10))

f = "name:{n}, age:{a}"  # 이름을 준다.
s = f.format_map({"n": "둘리", "a": 10})  # 딕셔너리 준다.. 딕셔너리: 키, 값 키값.
print(s)

f = "name:{n}, age:{a}"  # 이름을 준다.
s = f.format_map({"a": 10, "n": "둘리"})  # 딕셔너리 준다.. 딕셔너리: 키, 값 키값.
print(s)

# 생성
l1 = []  # l은 리스트 변환에 쓰는 거기때문에 워닝 준것이다.
l1 = [1, True, 'python', 3.14]

# 인덱싱
print(l1[0], l1[1], l1[2], l1[3])
print(l1[-4], l1[-3], l1[-2], l1[-1])

# slicing
print(l1[1:4]) # 1인덱스부터 3인덱스 앞까지.  # 3-1 개 나온다.
print(l1[1:4:1]) # 1을 생략한것이다.. 하나씩 잘라내는거임.

print(l1[:]) # 전부.. 잘라냄
print(l1[2:]) # 2번 인덱스부터 끝까지.
print(l1[3::-1]) #역방향.. 뒤집힘. 3인덱스부터.
print(l1[len(l1)-1::-1])  # 뒤집기.

# e = [2, 3]
# print(e.bit_length())  # 숫자?

# 반복
l2 = l1 * 2
print(l2)

# 연결
l2 = l1 + [1,2,3]  # 뒤에 붙인다.
print(l2)

#길이
print(len(l1))

# in, not in 확인.  # 스트링이랑 비슷하다.
print(5 in l2)
print(5 not in l2)
print('python' in l2)

#print(l2.__sizeof__())

#삭제  #스트링은 삭제안됨.. 리스트에는 가능
del l2[2]  # 2번 인덱스를 날린다.. 'python' 날라간다.
print(l2)
#print(l2.__sizeof__())

# 변경가능한 객체(mutable)
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90  # 10이 100이 되었다.// 100을 가르키게 되었다.
print(a)

# 슬라이싱을 사용한 치환.  # 스트링에서는 자바를 파이썬으로 replace했었다.  여기는 리스트.
a = [1, 12, 123, 1234]

a[0:2] = [10, 20] #0인덱스 1인덱스 바꾼다.. 2개.
print(a)

a[0:2] = [100]
print(a)  # 0, 1 인덱스가 100 하나로 쭐어든다.. 총 3개가 된다.

a[1:2] = [200]   # [] 는 리스트 표현,  1인덱스를 200으로바꿈
print(a)

a[2:3] = [300,400, 500]  # 300, 400을 2인덱스에다가 넣어준다.
print(a)

# 슬라이싱을 사용한 삭제
a = [1, 12, 123, 1234]

a[1:2] = [] # 빈배열을 넣어줌.. del 키워드로 삭제했었는데. 이게 더 쉬워보인다.
print(a)

a[0:] = []  #0부터 전체 다 선택함.
print(a)
# 리스트: 시퀀스니까 삭제하면 데이터가 막 움직일려나.
#print(a.__sizeof__())

#
# 슬라이싱을 사용한 삽입
#
a = [1, 12, 123, 1234]

# 중간삽입
a[1:1:] = ['a']
print(a)

# 마지막 삽입
a[5:] = [12345]
print(a)
a[len(a):] = [123456]
print(a)

# 처음에 삽입
a[:0] = [0]  # 0을 빼버리면 전체가 변경이된다.
print(a)

# 여러개 삽입
a[2:2] = [-12, -1, 0]  # 2번째 인덱스 앞에다가 넣어준다.
print(a)

# 10분휴식후,.
#
# 객체함수
#
  # 이번엔 메소드 사용..
a = [1,2,3]
  # 슬라이싱해도 되고, 메소드 써도 되고.

# 중간삽입
a.insert(1,2); # 메소드 쓰는게 편할 수 있겠다.
print(a) # 1번째 인덱스 위치에 2를 넣는다. 그 원래것들은 뒤로 밀린다.. (시간복잡도?)

# 뒤에 삽입
a.append(5)  #맨 뒤에 추가한다.
print(a)

# 앞에 삽입
a.insert(0, 0) # 0번째에 0을 넣는다.
print(a)

# reverse
a.reverse() # a를 거꾸로.. 한다.
print(a)

# 제거(값으로 삭제_
a.remove(3) # 3을 삭제..
print(a)   # 값이 삭제 된다.
# a.remove(3) # 값이 없는 경우 예외 발생.
#print(a)  # 에러가 뜬다.

# 확장
a.extend([-1, -2, -3]) # 메소드는 이름을 알고있어야 한다.
print(a)
a.append([2,4])  #원소를 추가하는데,, 리스트가 원소로 들어간다.
print(a)
#a.extend(5); 에러 발생..  # 리스트로 주면 된다.
a.extend([5])
print(a)

# stack 사용하기
s  = []
s.append(10) # 스택에 10이 들어감.  # push
s.append(20) # push
s.append(30)  #push

print(s)

print(s.pop())  # 끄집어냄... 빠짐.. pop은 빼내면서 리턴해준다.  # pop
##print(s)  # pop 된 상태를 나타낸다.
print(s.pop())
print(s)  # 처음들어간거 밑바닥에 있던거 하나 있다... (실생활이랑 비슷한 모양이다. - 물리, 철학, 관념, 메소드.)

# queue 사용하기
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)  # 순서대로,, 인덱스 큰것이 나중에 들어온것이다.

print(a)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
# 마지막에 들어간 두개만 남아있겠다.
print((q))

# sort(): 내장된 정렬 알고리즘에 따라 정렬
l = [1, 5, 3, 9, 8, 11] #  리스트이네
l.sort()
print(l)  # 오름차순으로 정렬되있네..

l.sort(reverse=True)  # 리버스 생략 되있음.
print(l)  # 뒤집어서 정렬.... 내림차순이 된다.

l = [10, 2, 33, 9, 8, 33, 4, 11]
l.sort(key=str)  # key를 스트링으로봐라..  #일단 워닝 무시
print(l)

l.sort(key=int)  #객체함수로 소팅한다.
print(l) # 정수로 봐서 정렬한다..

# 전역함수를 사용한다.  sorted
l = [19, 46, 37, 28, 91, 55, 64]
l2 = sorted(l)   # 소티드 전역함수,, 새로운 객체 생성해서 l2에 넣는다.
print(l2)

l2 = sorted(l, reverse=True)  # 거꾸로,, 내림차순정렬
print(l2)

l = [19, 46, 37, 28, 91, 55, 64]
def f(i):
    return i % 10    # 일의자리만 출력해주네.

print(f(12))

l2 = sorted(l, key=f, reverse=True)  # 컴페어함수야?? 이 함수를 키로 써라,,  # 일의자리로 비교한다.. 키값으로 비교한다.
# 키 스트링이면, 스트링값으로 비교..
print(l2)  # 내림차순, ,일의자리.

l2 = sorted(l, key = f, reverse=False)
print(l2)


















