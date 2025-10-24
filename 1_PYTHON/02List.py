# 리스트
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])   # apple
# print(fruits[1])   # banana
# # fruits[5]="melon" # 리스트 범위를 넘어선 인덱스는 추가 X (자바스크립트에서는 가능)
# fruits.append("orange")
# print(fruits)
#
# # 빈 리스트
# a = []
# b = list()
#
# # 초기 값 포함
# nums = [1, 2, 3, 4, 5]
#
# # 다른 자료형도 혼합 가능
# mixed = [1, "hi", 3.14, True]
#
# nums = [10, 20, 30, 40, 50]
#
# print(nums[0])     # 10
# print(nums[-1])    # 50 (뒤에서 첫 번째)
# print(nums[1:4])   # [20, 30, 40] # 맨 끝 값제외 (4-1 인덱스까지)
# print(nums[0:-1])   # [10, 20, 30, 40] - 음수값으로 지정 가능 단 시작값을 잘 설정
# print(nums[:3])    # [10, 20, 30] : (3-1)인덱스까지
# print(nums[::2])   # [10, 30, 50] (2칸씩 건너뛰기)
#
# fruits = ["apple", "banana", "cherry"]
#
# fruits.append("orange")   # 마지막에 추가
#
# fruits.insert(1, "grape") # 인덱스 1에 삽입
# print(fruits) # ['apple', 'grape', 'banana', 'cherry', 'orange']
#
# fruits.remove("banana")   # 특정 값 제거
# print(fruits) # ['apple', 'grape', 'cherry', 'orange']
#
# popped = fruits.pop()     # 마지막 요소 꺼내기
# print("popped:", popped) # popped: orange
#
# fruits.sort()      # 오름차순 정렬
# print(fruits)      # ['apple', 'cherry', 'grape']
# fruits.reverse()    # 반대로 뒤집기
# print(fruits)       # ['grape', 'cherry', 'apple']
#
# count = fruits.count("apple")   # 개수 세기
# print(count) # 1
# index = fruits.index("cherry")  # 위치 찾기
# print(index) # 1 (마지막 reverse 작동으로 1번 인덱스에 위치해있음)

# # 리스트와 반복문
# nums = [1, 2, 3, 4, 5]
#
# # for문
# for n in nums:
#     print(n)
#
# # enumerate 사용 - 열거용
# for i, n in enumerate(nums):
#     print(i, n) # (i : 인덱스, n : nums의 값)
#
# # 리스트 컴프리헨션
# # 1~5 제곱수
# squares = [x**2 for x in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]
#
# # 짝수만 선택
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)  # [0, 2, 4, 6, 8]
#
# # 2차원 리스트
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[0])  # [1, 2, 3] 0번째 행
# print(matrix[0][1])  # 2 [0번째 행][1번째 열]
# print(matrix[2][2])  # 9
#
# # 중첩 반복문으로 출력
# for row in matrix: # 행
#     for val in row: # 열
#         print(val, end=" ")
#     print()
#
# # 리스트 복사
# a = [1, 2, 3]
# # Object -
# b = a          # 얕은 복사 (같은 객체)
# c = a[:]       # 슬라이싱으로 복사 (새로운 객체) 전범위복사
# d = list(a)    # list()로 복사 : 참조복사(주소복사)
#
# a[0] = 100
# print("a:", a)  # [100, 2, 3]
# print("b:", b)  # [100, 2, 3] → 같은 객체라서 같이 변경됨
# print("c:", c)  # [1, 2, 3]
# print("d:", d)  # [1, 2, 3]
#
# # a와 b는 같은 위치

# # 문제1
# li = [10, 20, 30, 40, 50]
# print(li[0], li[-1])
#
# # 문제2
# li2 = [1, 2, 3]
# li2.append(4)
# li2.append(5)
# print(li2)
#
# # 문제3
# li3 = [3, 6, 9, 12, 15]
# print(li3[1:4])
#
# # 문제4
# li4 = [5, 2, 9, 1, 7]
# li4.sort()
# print(li4)
# li4.reverse()
# print(li4)
#
# # 문제5
# li5 = [n**2 for n in range(1,6)]
# print(li5)

# # --------------------------------
# # 딕셔너리
# # {'key' : 'value"} 형태
# person = {"name": "Alice", "age": 25, "city": "Seoul", "name":"hong"} # 중복된 key가 있다면 마지막 key가 덮어쓰게 됨
# print(person["name"])  # Alice -> name key 값을 마지막에 추가하면 결과는 hong
#
# # 기본 생성
# d1 = {"a": 1, "b": 2}
#
# # dict() 함수 활용
# d2 = dict(a=1, b=2)
#
# # 리스트/튜플 쌍을 변환
# d3 = dict([("a", 1), ("b", 2)])
#
# print(d1, d2, d3)

# person = {"name": "Alice", "age": 25, "city": "Seoul"}
#
# # 키, 값, 쌍
# print(person.keys())     # dict_keys(['name', 'age', 'city'])
# print(person.values())   # dict_values(['Alice', 25, 'Seoul'])
# print(person.items())    # dict_items([('name','Alice'),('age',25),('city','Seoul')])
#
# # get() : 키 없을 때 None 반환
# print(person.get("age"))       # 25
# print(person.get("country"))   # None
# print(person.get("country", "없음"))  # 없음
#
# # pop() : 특정 키 제거 + 값 반환
# age = person.pop("age")
# print(age, person) # 25 {'name': 'Alice', 'city': 'Seoul'}
#
# # update() : 다른 딕셔너리 병합
# person.update({"job": "teacher"})
# print(person) # {'name': 'Alice', 'city': 'Seoul', 'job': 'teacher'}

# ----------------------------------
# # 반복문과 딕셔너리
# scores = {"kim": 90, "lee": 85, "park": 95}
#
# # 키만 반복
# for k in scores:
#     print(k)
#
# # 값만 반복
# for v in scores.values():
#     print(v)
#
# # 키와 값 동시 반복
# for k, v in scores.items():
#     print(k, v)

# --------------------------------------
# # 딕셔너리 컴프리 헨션
# # 1~5까지 제곱 딕셔너리 만들기
# s = [x**2 for x in range(1, 6)]
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)   # {1:1, 2:4, 3:9, 4:16, 5:25}
#
# # 조건 추가
# evens = {x: x**2 for x in range(1, 6) if x % 2 == 0}
# print(evens)     # {2:4, 4:16}

# # 중첩 딕셔너리!!!!!!!!!
# # 딕셔너리 안에 딕셔너리 or 딕셔너리 안에 리스트 형태로 많이 사용
# students = {
#     "kim": {"age": 20, "major": "CS"},
#     "lee": {"age": 22, "major": "Math"}
# }
#
# print(students["kim"]["major"])  # CS
# print(students["kim"])  # {'age': 20, 'major': 'CS'}
#
# s = {
#     "K1" : ["V1-1", "V1-2", "V1-3"],
#     "K2" : ["V2-1", "V2-2", "V2-3"],
#     "K3" : ["V3-1", "V3-2", "V3-3"],
# }
# print(s['K1']) # ['V1-1', 'V1-2', 'V1-3']
# print(s['K1'][-1]) # V1-3

# # 딕셔너리 반복문
# person_info = {
#     'name': '사랑',
#     'age': 20,
#     'city': '부산',
#     'hobbies': ['연애', '수영', '코딩']
# }
# # zip() : 튜플 만드는 함수 (= person_info.items() 로 사용가능)
# for k, v in zip(person_info.keys(), person_info.values()):
#     print(k, v)
#
# for k, v in person_info.items():
#     print(k, v)

# # 문제1
# di = {"name" : "kim", "age" : 20, "city":"seoul"}
# print(di['name'])
# print(di['city'])
#
# # 문제2
# di2 = {}
# di2.update({'math':90, "eng" : 85})
# print(di2)
#
# # 문제3
# di3 = {'a':1, 'b':2, 'c':3}
# print(di3.keys())
# print(di3.values())
# print(di.keys(), di.values())
#
# # 문제4
# di4 = {"apple":1000, "banana":2000, "cherry":3000}
# di4['banana'] = 2500
# di4['orange'] = 1500
# print(di4)
#
# # 문제5
# di5 = {x: x**2 for x in range(1, 6)}
# print(di5)

# # 튜플 생성방법
# # 기본 생성
# a = (1, 2, 3)
#
# # 소괄호 생략 가능
# b = 4, 5, 6
#
# # 요소가 하나일 때는 반드시 콤마 필요
# c = (7,)
# d = 7,
# e = 7  # 콤마가 없으며 튜플이 X
# print(type(d))
# print(type(e))
#
# # 빈 튜플
# empty = ()
# print(a, b, c, d, empty)  # (1, 2, 3) (4, 5, 6) (7,) (7,) ()
#
# # --------------------
# # 패킹과 언패킹
# # 패킹: 여러 값을 하나의 튜플로 묶음
# t = 1, 2, 3
#
# # 언패킹: 튜플을 여러 변수에 나눠 담음
# a, b, c = t
# print(a, b, c)   # 1 2 3
#
# # *을 이용한 언패킹
# nums = (1, 2, 3, 4, 5)
# x, y, *rest = nums
# print(x, y, rest)  # 1 2 [3,4,5]
#
# # -----------------
# # 튜플과 함수 반환값
# def calc(a, b):
#     return a+b, a*b
#
# print(calc(10, 20)) # (30, 200)
# print(type(calc(10, 20))) # <class 'tuple'>
#
#
# result = calc(3, 4)
# print(result)        # (7, 12)
#
# s, m = calc(3, 4)    # 튜플 형태를 언패킹
# print(s, m)          # 7 12

# # --------------------
# # 튜플 활용
# d = {(1,2): "point A", (3,4): "point B"}
# print(d[(1,2)])   # point A

# # 문제1
# t = (10, 20, 30, 40, 50)
# print(t[0], t[2])
#
# # 문제2
# t2 = (1, 2, 3)
# t3 = (4, 5)
# print(t2 + t3)
#
# # 문제3
# t4 = (100, 200, 300, 400, 500)
# print(t4[1:4])
#
# # 문제4
# t5 = (1, 2, 3)
# a, b, c = t5
# print(a, b, c)

# # 문제5
# def calc(x, y):
#     return x+y, x*y
#
# a, b = calc(10, 20)
# print(a, b)
#
# # 인덱싱과 슬라이싱
# data = ["a", "b", "c", "d", "e"]
#
# print(data[0])   # 첫 번째 요소 → a
# print(data[2])   # 세 번째 요소 → c
# print(data[-1])  # 마지막 요소 → e
# print(data[-2])  # 뒤에서 두 번째 → d
#
# nums = [10, 20, 30, 40, 50]
#
# print(nums[1:4])    # 인덱스 1~3 → [20, 30, 40]
# print(nums[:3])     # 처음부터 인덱스 2까지 → [10, 20, 30]
# print(nums[2:])     # 인덱스 2부터 끝까지 → [30, 40, 50]
# print(nums[::2])    # 처음부터 끝까지, 2칸씩 → [10, 30, 50]
# print(nums[::-1])   # 거꾸로 뒤집기 → [50, 40, 30, 20, 10]
#
# text = "Python"
#
# print(text[0])     # P
# print(text[-1])    # n
# print(text[1:4])   # yth
# print(text[::-1])  # nohtyP
#
# t = (100, 200, 300, 400)
#
# print(t[0])      # 100
# print(t[1:3])    # (200, 300)
# print(t[::-1])   # (400, 300, 200, 100)
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[0][1])   # 첫 번째 행, 두 번째 값 → 2
# print(matrix[2][2])   # 세 번째 행, 세 번째 값 → 9

# # 문제1
# li = ["a", "b", "c", "d", "e"]
# print(li[0], li[-1])

# # 문제2
# li2 = [10, 20, 30, 40, 50]
# print(li2[1:4])
#
# # 문제3
# str = "Python"
# print(str[0], str[-1])
#
# # 문제4
# tu = (100, 200, 300, 400, 500)
# print(tu[::2])
#
# # 문제5
# li3 = [1, 2, 3, 4, 5]
# print(li3[::-1])

# --------------------
# # 파이썬 내장함수
# li = [3, 7, 1, 9, 5]
# print(sum(li)) # 25
#
# li2 = [12, 45, 7, 23, 89]
# print(max(li2)) # 89
# print(min(li2)) # 7
#
# str = "Hello Python"
# print(len(str)) # 12
#
# fl = 3.14159
# print(round(fl,2)) # 3.14
#
# li3 = [True, False, True, True]
# print(sum(li3)) # 3

# --------------
# # 문자열
# text = "빅데이터 분석기사 파이썬 공부"
# # print(text.replace("공부", "스터디"))
#
# text = text.replace("분석기사", "분석을 위한").replace("파이썬", "머신러닝")
# print(text)
#
# text2 = "안녕하세요! 함께 성장해요."
# print(text2[0:2])
# print(text2[7:10])
# print(text2[::-1])

# date = "2022-12-25"
# print(date[5:7], date[8:])
# print(date.split("-"))
#
# li = ["빅데이터", "머신러닝", "딥러닝"]
# print(" ".join(li))
# print("-".join(li))


# ----------------
# # 함수
# def greeting():
#     print("파이썬 함수 시작!")
#
# # 함수 여러 번 호출
# greeting()
# greeting()
#
# def greeting(n1, n2):
#     print("파이썬 함수 시작!")
#
# # 함수 여러 번 호출
# greeting(1, 2)
# greeting(3, 4)

# ---------------------
# # 리턴이 있는 함수 - 여러 값 반환 -> 튜플 형태로 반환
# def multiply(x, y):
#     return x * y, x + y, x - y if x > y else y - x
#
# result = multiply(6, 7)
# print(result)   # (42, 13, 1)
#
# # 평균함수
# def average(numbers):
#     return sum(numbers) / len(numbers)
#
# scores = [80, 90, 70, 100]
# print("평균:", average(scores))   # 85.0

# -------------------------------
# # 기본값 매개변수
# def introduce(name, age=20):
#     print(f"이름: {name}, 나이: {age}")
#
# introduce("홍길동", 25) # 이름: 홍길동, 나이: 25
# introduce("김철수")   # 나이는 기본값 20 사용 - 이름: 김철수, 나이: 20

# introduce() # 함수에서 모든 매개변수의 기본값 정의가 되어있다면 사용가능

# ---------------------------
# # 가변 매개변수
# def total(*args):
#     print(args)
#     print(type(args)) # <class 'tuple'>
#     return sum(args)
#
# print(total(1, 2, 3))       # 6
# print(total(5, 10, 15, 20)) # 50

# ---------------------------
# # 키워드 매개변수
# def show_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
# show_info(name="Alice", age=25, city="Seoul", hobby=['여행', '등산', '독서'])
# # {'name': 'Alice', 'age': 25, 'city': 'Seoul', 'hobby': ['여행', '등산', '독서']}
# # <class 'dict'>

# # 기본 함수 정의와 호출
# def greet():
#     print("파이썬 함수 시작!")
# greet()
# greet()
# greet()
#
# # 매개변수 있는 함수
# def hello(name):
#     print(f"안녕하세요, {name}")
# hello("철수")
# hello("영희")
#
# def add(x, y):
#     return x + y
#
# print(add(30, 90))
#
#
#
# def min_max(data):
#     return min(data), max(data)
#
# li = [3, 8, 1, 7, 5]
# print(min_max(li)) # 튜플형태로 반환
# m1, m2 = min_max(li)
# print(m1, m2)
#
#
# def total(*args):
#     return sum(args)
#
# print(total(1, 2, 3))
# print(total(10, 20, 30, 40))