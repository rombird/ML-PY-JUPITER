# mymath.py
"""간단한 수학 유틸 모듈"""

PI = 3.141592653589793

def add(a: float, b: float) -> float:
    """두 수의 합을 반환"""
    return a + b

def circle_area(r: float) -> float:
    """원의 넓이: πr^2"""
    return PI * (r ** 2)

# 모듈 내에서도 실행 가능
if __name__ == "__main__":
    # 모듈을 스크립트처럼 직접 실행했을 때의 데모
    print("demo:", circle_area(2))

