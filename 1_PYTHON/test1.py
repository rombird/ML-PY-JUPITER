import requests

res = requests.get("https://www.naver.com/")
print(res.status_code) # 200 : 상태 코드
# print(res.json())
print(res.headers) # 응답으로 들어오는 헤더정보
print(res.headers.get('Content-Type'))