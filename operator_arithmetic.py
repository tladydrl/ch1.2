# 사칙연산
print(2 * 3)
print(2 + 3)
print(2 - 3)
print(2 / 3)  # 실제 나눗셈이 된다. # 다른언어는 0
print(2 / 3.0)  # 정수와 플롯형이 연산되야. 다른언어에서는 이러면 플롯.
print(2.0 / 3.0)

# //(몫연산자), **(지수승), %(나머지연산)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# divmod() 함수  # 나누기도하고 나머지도 하는 함수.
print(divmod(2, 3), type(divmod(2,3)))
t = divmod(2,3)
print(t, type(t))
a, b = divmod(2, 3)  # 튜플이 언패킹 된다. 튜플이 풀려서 a와 b로 간다.
print(isinstance(t, tuple))






