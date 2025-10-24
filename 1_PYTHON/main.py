# use_module.py (동일 폴더)
import mymath
import mymath as m # 별칭 지정 가능
from mymath import add # 모듈안의 특정함수만 참조해서 사용


print(mymath.add(2, 3))
print(mymath.circle_area(2)) # 원의 넓이 함수

# 별칭으로 함수 부르기
print(m.add(2,3))

# 모듈안의 특정함수만 불러오는 작업을 했기 때문에 가능한 코드
print(add(20, 30))
