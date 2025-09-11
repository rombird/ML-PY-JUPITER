# 주석
'''
HELLO WORLD
HELLO WORLD
'''

# # ---------------
# # 기본입출력
# name = input("이름을 입력하세요 : ")
# print("입력한 이름 : ", name)
# print("자료형 : ", type(name)) # str
#
# age = int(input("나이를 입력하세요 : "))
# print("내년 나이 : ", age + 1)
# # 파이썬은 모든 자료형이 클래스

# ---------------
# # 변수
# age = 39
# height = 1.75
# name = "Alice"
#
# #  변수 출력
# print(name)
# print(age)
# print(height)
#
# # 여러 변수 출력
# print("name:", name, "age:", age, "height:", height)
#
# # 문자열 포매팅 (f-string)
# print(f"[f-string] {name} - age={age}, height={height}")
#
# # 자료형 확인
# print(type(name))   # <class 'str'>
# print(type(age))    # <class 'int'>
# print(type(height)) # <class 'float'>
#
# # 변수 재할당
# age = '40세'
# print("새 나이:", age)
# print(type(age)) # str (수정된 자료형으로 바로 적용됨)
#
# # 변수 삭제
# del age
# # print(age)  # 오류 발생: age is not defined``` (defined : 메모리 공간 할당됨을 의미)

# # 여러 변수 한 줄 대입·언패킹·스왑
#
# # 1) 여러 변수에 한 줄 대입
# x, y, z = 10, 20, 30
# print(x, y, z)
#
# # 같은 값 대입
# a = b = c = 100
# print(a, b, c)
#
# # 값 교환 (스왑)
# x, y = y, x
# print("스왑 후:", x, y)
#
# # 언패킹 (리스트/튜플 분해)
# numbers = [1, 2, 3]
# n1, n2, n3 = numbers
# print(n1, n2, n3)
#
# # 확장 언패킹 (*)
# first, *rest = [10, 20, 30, 40, 50]
# print(first)   # 10
# print(rest)    # [20, 30, 40, 50]
#
# # 언패킹 응용: 마지막 값 따로 받기
# *start, end = [100, 200, 300, 400]
# print(start, end)  # [100, 200, 300] 400```
#
# # 문제
# a, b, c = 1, 2, 3
# a, b, c = b, c, a
# print(f'a = {a}, b = {b}, c = {c}')
#
# x, y, *rest = [5, 10, 15, 20, 25]
# print(f'x = {x}, y = {y}, rest = {rest}')
#
# m = 100
# n = 200
# m, n = n, m
# print(f'm = {m}, n = {n}, m + n = {m+n}')

# ------------------------------------
# # 형변환
# # 문자열 → 정수
# a = int("10")
# print(a, type(a))   # 10 <class 'int'>
#
# # 문자열 → 실수
# b = float("3.14")
# print(b, type(b))   # 3.14 <class 'float'>
#
# # 숫자 → 문자열
# c = str(123)
# print(c, type(c))   # "123" <class 'str'>
#
# # Java 에서는 true, false 예약어 Python에서는 True, False 예약어
# print(bool(0))      # False
# print(bool(1))      # True (0이 아닌 모든 값)
# print(bool(""))     # False (빈 문자열)
# print(bool("0"))    # True  (문자열 "0"은 내용이 있으므로 True)
# print(bool([]))     # False (빈 리스트)
# print(bool([1]))    # True

# ------------------------------
# # 컬렉션
# data = [1, 2, 2, 3]
#
# # list → set (중복 제거)
# s = set(data)
# print(s, type(s))   # {1,2,3}
#
# # set → list
# l = list(s)
# l[0] = 100
# print(l, type(l))   # [1,2,3]
#
# # tuple 변환
# t = tuple(data)
# # t[0] = 100 # 값 변경 불가
# print(t, type(t))   # (1,2,2,3)
#
# # JSON 타입과는 조금 다름 JSON 타입은 key, value 모두 문자열
# # 딕셔너리
# d = {"a": 1, "b": 2, "c": 3}
# print("!!!", d, type(d)) # <class 'dict'>
# # 키만 리스트로
# keys = list(d)
# print(keys)   # ['a', 'b', 'c']
#
# # 값만 리스트로
# values = list(d.values())
# print(values) # [1, 2, 3]
#
# # 키-값 쌍 튜플로
# items = list(d.items())
# print(items)  # [('a',1), ('b',2), ('c',3)]
#
# dic = {'a':1, 'b':2}
# keys = list(dic.keys())
# values = list(dic.values())
# print(f'keys : {keys}, values : {values}')
#
# items = list(dic.items())
# print(items)

# -----------------------
# # 연산자
# # 덧셈, 뺄셈, 곱셈, 나눗셈
# a, b = 7, 2
# print("a + b =", a + b)    # 9
# print("a - b =", a - b)    # 5
# print("a * b =", a * b)    # 14
# print("a / b =", a / b)    # 3.5  (항상 실수)
#
# # 몫, 나머지, 거듭제곱
# print("a // b =", a // b)  # 3
# print("a % b  =", a % b)   # 1
# print("2 ** 3 =", 2 ** 3)  # 8
#
# x, y = 5, 3
# print("x == y :", x == y)   # False
# print("x != y :", x != y)   # True
# print("x >  y :", x > y)    # True
# print("x <  y :", x < y)    # False
# print("x >= y :", x >= y)   # True
# print("x <= y :", x <= y)   # False
#
# # 체이닝(파이썬만의 문법) -- Java에서는 사용 X
# n = 4
# print(3 < n < 10)    # True (3 < n and n < 10)
#
# a, b = True, False
# print("a and b :", a and b)    # False
# print("a or b :", a or b)     # True
# print("not a   :", not a)      # False
#
# # 단락 평가(short-circuit) 예시
# def f(): # 함수 선언
#     print("f() called")
#     return True
#
# print(False and f())  # False (f()는 호출되지 않음)
# print(True or f())    # True  (f()는 호출되지 않음)
# print(f()) # True(f() 호출됨)
#
# # 대입/복합 대입 연산자
# x = 10      # 대입
# x += 5      # 15
# x -= 3      # 12
# x *= 2      # 24
# x /= 4      # 6.0 (실수 주의)
# x //= 2     # 3
# x %= 2      # 1
# x **= 5     # 1 ** 5 = 1
# print("x =", x)
#
# # 문자열/리스트에도 사용 가능
# s = "ha"
# s *= 3
# print(s)    # "hahaha"
#
# arr = [1]
# arr *= 3 # [1]*3
# print(arr)  # [1, 1, 1]
#
# # 2진수로 보기 좋게 출력 -> bin()
# n = 13
# print("n      :", n, bin(n))         # 13 0b1101
# print("n<<2   :", n << 2, bin(n<<2)) # 52 0b110100
# print("n>>1   :", n >> 1, bin(n>>1)) # 6  0b110
#
#
# # -------------------------
# # 멤버십/식별 연산자
# # 멤버십: in / not in
# text = "apple"
# print("'a' in text     :", "a" in text)      # True
# print("'x' not in text :", "x" not in text)  # True
#
# nums = [1, 2, 3]
# print("2 in nums      :", 2 in nums)         # True
# print("4 not in nums  :", 4 not in nums)     # True
#
# # 식별: is / is not  (객체 동일성)
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
#                               # 파이썬은 클래스 자료형 이걸로 만든 대상은 모두 객체(객체 위치정보를 다 담고 있다)
# print("a == b  :", a == b)    # 값(내용)은 같다(값의 일치여부) -> True
# print("a is b  :", a is b)    # 객체(참조)는 다르다 -> False(Object의 위치정보는 다르기 때문에)
# print("a is c  :", a is c)    # 같은 객체 참조 -> True
#
# # 작은 정수/짧은 문자열 캐싱으로 is가 True처럼 보일 수 있으니 ==와 구분할 것
# s1 = "py"
# s2 = "py"
# print("s1 == s2:", s1 == s2)  # True (값 비교)
# print("s1 is s2:", s1 is s2)  # (환경별 최적화 영향) 동일성 보장은 아님

# # 문제
# score_kor = 88
# score_eng = 92
# score_math = 79
# avg = (score_kor + score_eng + score_math)/3
# print(f'평균 점수 : {avg:.2f}')
#
# passed = (avg >= 90 and (score_kor>=70 and score_eng>=70 and score_math >= 70))
# print("passed : ", passed)
#
# users = ['kim', 'lee', 'park']
# print("lee가 포함되어 있는지 : ", "lee" in users)
#
# x = [1, 2]
# y = x
# z = [1, 2]
# print(x is y) # True
# print(x is z) # False

# ----------------------------------------
# # 분기문
# x = 10
#
# if x > 5:
#     print("x는 5보다 크다")  # 조건이 True라면 실행
#
# if x > 5:
#     print("x는 5보다 크다")  # 들여쓰기는 일치
#     print("TEST")
#
# # 줄 정렬 ctrl + alt + L
#
# # if - elif - else문
# num = 0
#
# if num > 0:
#     print("양수")
# elif num < 0:
#     print("음수")
# else:
#     print("0입니다.")
#
# # 삼항연산자 조건 표현식
# score = 85
# result = "합격" if score >= 60 else "불합격"
# print(result)   # 합격
#
# # 논리연산자
# age = 25
# is_student = True
#
# if age >= 20 and is_student:
#     print("성인 학생입니다.")
#
# # in 연산자 활용
# fruit = "apple"
#
# if fruit in ["apple", "banana", "cherry"]:
#     print(f"{fruit}은(는) 과일 목록에 있습니다.")
#
# # pass 문
# x = 10
#
# if x > 0:
#     pass   # 아직 로직 미작성, 오류 없이 넘어감
# else:
#     print("x는 0 이하")
#
# # 예외적인 케이스 처리
# value = input("숫자를 입력하세요: ")
#
# if value.isdigit(): # 전달받은 형태가 int 형태이면
#     num = int(value)
#     print("입력한 숫자:", num)
# else:
#     print("숫자가 아닙니다.")
#
# 문제
# price = int(input("구매 금액 : "))
# if price >= 100000:
#     print("10% 할인 적용")
# elif price >= 50000:
#     print("5% 할인 적용")
# else:
#     print("할인 없음")
#
# num = int(input("정수를 입력하세요 >>> "))
# if num % 2 == 0 and num > 0:
#     print("양의 짝수")
# elif num % 2 != 0 and num > 0:
#     print("양의 홀수")
# elif num < 0:
#     print("음수")
# else:
#     print("0입니다")
# 중첩문을 이용하면
# if num>0:
#     if num % 2 == 0:
#         print("양의 짝수")
#     else:
#         print("양의 홀수")
# elif num < 0:
#     print("음수")
# else:
#     print("0")
#
#
# num = int(input("정수를 입력하세요 >>> "))
# if num % 3 == 0 and num % 5 == 0:
#     print("3과 5의 공배수")
# elif num % 3 == 0:
#     print("3의 배수")
# elif num % 5 == 0:
#     print("5의 배수")
# else:
#     print("해당 없음")
#
# age = int(input("나이를 입력하세요 >>>>> "))
# student = input("학생 여부에 따라 yes/no를 입력하세요 >>>> ")
# if age >= 20 and student == "yes":
#     print("성인 학생")
# elif age >= 20 and student == "no":
#     print("성인 비학생")
# else:
#     print("미성년자")
# # 또 다른 답
# if age >= 20:
#     if student.lower() == "yes":
#         print("성인 학생")
#     else:
#         print("성인 비학생")
# else:
#     print("미성년자")

# ------------------------------------
# # 반복문
# # 리스트 반복
# # fruits = ["apple", "banana", "cherry"]
# fruits = ("apple", "banana", "cherry")
# for f in fruits:
#     print(f)
#
# # range()활용
# # range(시작num, 종료num, step)
# # 0부터 4까지 출력
# for i in range(5):
#     print(i)
#
# # 1부터 10까지 홀수 출력
# for i in range(1, 11, 2):
#     print(i)
#
# # While문
# count = 0
#
# while count < 5:
#     print("count =", count)
#     count += 1
#
# # break, continue
# # break 예시
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)   # 1~4 출력
#
# # continue 예시
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)   # 1, 2, 4, 5 출력
#
# # 중첩반복문
# for i in range(1, 4):       # 행
#     for j in range(1, 4):   # 열
#         print(f"({i},{j})", end=" ")
#     print()
#
# # else와 함께 쓰는 반복문
# # for문과 else
# for n in range(3, 5, 2):
#     if n % 2 == 0:
#         print("짝수 발견:", n)
#         break
#     else:
#         print("짝수 없음")
#
# # while문과 else
# x = 3
# while x > 0:
#     x -= 1
#     print("x =", x)
# else:
#     print("루프 종료")
#
# # 리스트 컴프리헨션 - 간략하게 반복문 처리하는 방식
# # 1~5 제곱수 리스트
# squares = [x**2 for x in range(1, 6)]
# print(squares)   # [1, 4, 9, 16, 25]
#
# # 조건부 컴프리헨션 (짝수만)
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)     # [0, 2, 4, 6, 8]
#
# # enumerate() 사용
# names = ["kim", "lee", "park"]
#
# for i, name in enumerate(names, start=1):
#     print(i, name)
# # 1 kim
# # 2 lee
# # 3 park

# # 문제 1
# for i in range(1, 11):
#     print(i, end=" ")

# # 문제 2
# sum = 0
# for i in [3, 7, 2, 9, 4]:
#     sum += i
# print(sum)
#
# # 문제 3
# num = 5
# while num > 0:
#     print(num, end=' ')
#     num -= 1

# # 문제 4
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, end=' ')
# print()
# # 문제 5
# dan = 3
# print("구구단 3단")
# for i in range(1, 10):
#     print(f'{dan} x {i} = {dan * i} ')














